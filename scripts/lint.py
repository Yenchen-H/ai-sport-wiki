#!/usr/bin/env python3
"""LLM Wiki 程式檢查（lint）

用法：
    python3 scripts/lint.py            # 一般檢查，來源少於 5 篇只警告
    python3 scripts/lint.py --final    # 最終檢查，來源少於 5 篇算錯誤

檢查項目（對應 AGENTS.md 任務 B）：
  1. frontmatter 欄位齊全
  2. 出處格式必須是 [作者 年份, p.頁碼]
  3. 來源頁、概念頁的每個事實句都有出處
  4. 引用的來源存在（wiki/sources/ 有頁面、raw/ 有 PDF）
  5. 頁碼沒有超過 PDF 總頁數
  6. 英文原文引用能在該頁 PDF 文字中逐字找到
  7. 內部連結沒有斷
  8. index.md 列出所有頁面；沒有孤兒頁
  9. 「⚠ 說法分歧」段落至少有 2 個不同出處（不同來源，或同一來源的不同頁）
 10. 來源數至少 5 篇
需要 poppler 的 pdftotext / pdfinfo。
"""
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
FINAL = "--final" in sys.argv

CITE = re.compile(r"\[([A-Z][A-Za-z\-]+) (\d{4}), p\.(\d+)(?:[–-](\d+))?\]")
# 長得像出處但格式不對：[Zhou 2025]、[Zhou, 2025, p4] 之類（排除 Markdown 連結）
CITE_LIKE = re.compile(r"\[[A-Z][^\[\]]*?\d{4}[^\[\]]*?\](?!\()")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
QUOTE = re.compile(r"[\"“]([^\"”]{15,})[\"”]")
EXEMPT_HEADINGS = ("相關", "書目")
REQUIRED_FM = ("type", "title", "sources", "updated")

errors, warnings = [], []
_page_cache, _count_cache = {}, {}


def rel(p):
    return p.relative_to(ROOT).as_posix()


def norm(text):
    text = unicodedata.normalize("NFKC", text).lower()
    return re.sub(r"[^a-z0-9]", "", text)


def pdf_pages(pdf):
    if pdf not in _count_cache:
        out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
        m = re.search(r"Pages:\s+(\d+)", out)
        _count_cache[pdf] = int(m.group(1)) if m else 0
    return _count_cache[pdf]


def pdf_text(pdf, page):
    key = (pdf, page)
    if key not in _page_cache:
        out = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), str(pdf), "-"],
                             capture_output=True, text=True).stdout
        _page_cache[key] = norm(out)
    return _page_cache[key]


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    fm = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.split("#")[0].strip()
    return fm, text[end + 4:]


def source_id(name, year):
    return f"{name.lower()}{year}"


pages = sorted(p for p in WIKI.rglob("*.md") if p.name not in ("index.md", "log.md"))
source_pages = {p.stem for p in (WIKI / "sources").glob("*.md")}
inbound = {p: set() for p in pages}
index_text = (WIKI / "index.md").read_text(encoding="utf-8") if (WIKI / "index.md").exists() else ""

for page in pages + [WIKI / "index.md", WIKI / "log.md"]:
    if not page.exists():
        errors.append(f"{rel(page)}：檔案不存在")
        continue
    text = page.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    is_content = page in pages
    ptype = (fm or {}).get("type", "")

    # 1. frontmatter
    if is_content:
        if fm is None:
            errors.append(f"{rel(page)}：缺少 frontmatter")
        else:
            for k in REQUIRED_FM:
                if not fm.get(k):
                    errors.append(f"{rel(page)}：frontmatter 缺少 {k}")

    heading = ""
    in_code = False
    disagreement_block = None  # (起始行號, 引用來源集合)

    def close_block():
        if disagreement_block and len(disagreement_block[1]) < 2:
            errors.append(f"{rel(page)}:{disagreement_block[0]}：「⚠ 說法分歧」段落只有 "
                          f"{len(disagreement_block[1])} 個不同出處，至少要 2 個")

    body_offset = text[: len(text) - len(body)].count("\n")
    for i, line in enumerate(body.splitlines(), start=body_offset + 1):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s:
            continue
        if s.startswith("#"):
            close_block()
            disagreement_block = None
            heading = s
            continue

        cites = CITE.findall(s)

        # 2. 格式錯誤的出處
        for cand in CITE_LIKE.findall(s):
            if not CITE.fullmatch(cand):
                errors.append(f"{rel(page)}:{i}：出處格式錯誤 {cand}（應為 [作者 年份, p.頁碼]）")

        # 4、5. 來源存在、頁碼範圍
        for name, year, p1, p2 in cites:
            sid = source_id(name, year)
            pdf = RAW / f"{sid}.pdf"
            if sid not in source_pages:
                errors.append(f"{rel(page)}:{i}：引用 [{name} {year}] 但 wiki/sources/{sid}.md 不存在")
            if not pdf.exists():
                errors.append(f"{rel(page)}:{i}：引用 [{name} {year}] 但 raw/{sid}.pdf 不存在")
                continue
            n = pdf_pages(pdf)
            for p in filter(None, (p1, p2)):
                if not 1 <= int(p) <= n:
                    errors.append(f"{rel(page)}:{i}：[{name} {year}, p.{p}] 超出 PDF 頁數（共 {n} 頁）")

        # 6. 原文引用逐字比對（引號後面的第一個出處）
        for m in QUOTE.finditer(s):
            quote = m.group(1)
            if not re.search(r"[A-Za-z]{3,}", quote):
                continue
            after = CITE.search(s, m.end())
            if not after:
                errors.append(f"{rel(page)}:{i}：英文引用沒有出處：\"{quote[:40]}…\"")
                continue
            name, year, p1, p2 = after.groups()
            pdf = RAW / f"{source_id(name, year)}.pdf"
            if not pdf.exists():
                continue
            last = int(p2 or p1)
            hay = "".join(pdf_text(pdf, p) for p in range(int(p1), min(last, pdf_pages(pdf)) + 1))
            if norm(quote) not in hay:
                errors.append(f"{rel(page)}:{i}：引用原文在 [{name} {year}, p.{p1}] 找不到："
                              f"\"{quote[:50]}…\"")

        # 3. 事實句要有出處（來源頁、概念頁）
        if is_content and ptype in ("source", "concept") and not any(h in heading for h in EXEMPT_HEADINGS):
            only_links = LINK.sub("", s).strip(" -*|:：、,，") == ""
            table_rule = set(s) <= set("|-: ")
            if not cites and not only_links and not table_rule and not s.startswith(">"):
                errors.append(f"{rel(page)}:{i}：這句沒有出處 → {s[:50]}")

        # 9. 說法分歧
        if is_content and "⚠" in s and "說法分歧" in s:
            close_block()
            disagreement_block = (i, set())
        if disagreement_block is not None:
            disagreement_block[1].update((source_id(n, y), p1) for n, y, p1, _ in cites)

        # 7. 內部連結
        for target in LINK.findall(s):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            dest = (page.parent / target.split("#")[0]).resolve()
            if not dest.exists():
                errors.append(f"{rel(page)}:{i}：連結斷了 → {target}")
            elif dest in inbound and page.name != "index.md" and dest != page:
                inbound[dest].add(page)
    close_block()

# 8. index 完整、孤兒頁
for p in pages:
    link = p.relative_to(WIKI).as_posix()
    if f"({link})" not in index_text:
        errors.append(f"wiki/index.md：沒有列出 {link}")
    if not inbound[p] and p.parent.name != "sources":
        warnings.append(f"{rel(p)}：孤兒頁（除了 index 之外沒有其他頁面連到它）")

for sid in source_pages:
    if not (RAW / f"{sid}.pdf").exists():
        errors.append(f"wiki/sources/{sid}.md：raw/{sid}.pdf 不存在")

# 10. 來源數
msg = f"來源頁只有 {len(source_pages)} 篇，至少要 5 篇"
if len(source_pages) < 5:
    (errors if FINAL else warnings).append(msg)

print(f"LLM Wiki lint：{len(pages)} 個頁面、{len(source_pages)} 篇來源")
for w in warnings:
    print(f"  [警告] {w}")
for e in errors:
    print(f"  [錯誤] {e}")
print("結果：" + ("全部通過 ✅" if not errors else f"{len(errors)} 個錯誤 ❌"))
sys.exit(1 if errors else 0)
