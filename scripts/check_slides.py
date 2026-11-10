#!/usr/bin/env python3
"""簡報 graph 的程式檢查關卡（對應 .agents/skills/topic-slides/SKILL.md）

用法：python3 scripts/check_slides.py <關卡> slides/<主題>
  coverage  ② 覆蓋率關卡：sources.md 至少列出 3 個存在的 Wiki 頁
  cards     ③ 證據卡：每張卡只對應 1 個 Wiki 頁，卡上每句都逐字出現在該頁
  outline   ④ 大綱：8～15 張，每張列出的卡都存在
  drafts    ⑥ 逐頁稿：每頁 ≤5 個重點、每點 ≤40 字、有 Wiki 標註、出處都來自對應的卡
  render    ⑨ 渲染檢查：張數一致、每張有 Wiki 標註且檔案存在、1280×720 下沒有溢出（需要 playwright）
通過回傳 0，沒過回傳 1，並列出要退回哪一關。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CITE = re.compile(r"\[[A-Z][A-Za-z\-]+ \d{4}, p\.\d+(?:[–-]\d+)?\]")
errors = []


def strip_cites(s):
    return CITE.sub("", s).strip()


def bullet_text(s):
    return re.sub(r"^[-*]\s+", "", s.strip())


def parse_frontmatter(text):
    fm = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        for line in text[3:end].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
        text = text[end + 4:]
    return fm, text


def coverage(d):
    src = (d / "sources.md").read_text(encoding="utf-8")
    pages = re.findall(r"\]\((\.\./\.\./wiki/[^)]+\.md)\)", src)
    ok = [p for p in pages if (d / p).resolve().exists()]
    for p in set(pages) - set(ok):
        errors.append(f"sources.md：{p} 不存在 → 退回 ① 檢索")
    if len(set(ok)) < 3:
        errors.append(f"相關 Wiki 頁只有 {len(set(ok))} 頁（< 3）→ 停止，回報資料不足")
    return len(set(ok))


def load_cards(d):
    cards = {}
    for c in sorted((d / "cards").glob("*.md")):
        fm, body = parse_frontmatter(c.read_text(encoding="utf-8"))
        facts = [bullet_text(l) for l in body.splitlines() if l.strip().startswith("- ")]
        cards[c.stem] = (fm.get("wiki", ""), facts)
    return cards


def cards_check(d):
    cards = load_cards(d)
    if not cards:
        errors.append("cards/ 是空的 → 退回 ③")
    for name, (wiki, facts) in cards.items():
        page = (d / "cards" / wiki).resolve()
        if not wiki or not page.exists():
            errors.append(f"cards/{name}.md：wiki 欄位 {wiki!r} 不存在 → 退回 ③")
            continue
        text = page.read_text(encoding="utf-8")
        for f in facts:
            if f not in text:
                errors.append(f"cards/{name}.md：這句不在 {wiki} 原文中（只能逐字摘錄）→ 退回 ③：{f[:40]}")
            if not CITE.search(f):
                errors.append(f"cards/{name}.md：這句沒有原始出處 → 退回 ③：{f[:40]}")
    return cards


def load_outline(d):
    slides = []
    for line in (d / "outline.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s+(\d+)\.\s+(.+)$", line)
        if m:
            slides.append({"no": int(m.group(1)), "title": m.group(2), "cards": []})
        elif slides and line.strip().startswith("- 卡片："):
            slides[-1]["cards"] = [c.strip() for c in line.split("：", 1)[1].split("、") if c.strip()]
    return slides


def outline_check(d):
    cards = load_cards(d)
    slides = load_outline(d)
    if not 8 <= len(slides) <= 15:
        errors.append(f"大綱有 {len(slides)} 張，應為 8～15 張 → 退回 ④")
    for s in slides:
        for c in s["cards"]:
            if c != "（無）" and c not in cards:
                errors.append(f"大綱第 {s['no']} 張：卡片 {c} 不存在 → 退回 ③ 或 ④")
    return slides


def drafts_check(d):
    cards = load_cards(d)
    slides = outline_check(d)
    for s in slides:
        f = d / "drafts" / f"{s['no']:02d}.md"
        if not f.exists():
            errors.append(f"drafts/{f.name} 不存在 → 退回 ⑥")
            continue
        fm, body = parse_frontmatter(f.read_text(encoding="utf-8"))
        bullets = [bullet_text(l) for l in body.splitlines() if l.strip().startswith("- ")]
        if len(bullets) > 5:
            errors.append(f"drafts/{f.name}：{len(bullets)} 個重點（> 5）→ 退回 ⑥ 縮減")
        for b in bullets:
            n = len(strip_cites(b))
            if n > 40:
                errors.append(f"drafts/{f.name}：重點 {n} 字（> 40）→ 退回 ⑥ 縮短：{strip_cites(b)[:20]}…")
        wikis = [w.strip() for w in fm.get("wiki", "").split(",") if w.strip()]
        if s["cards"] != ["（無）"] and not wikis:
            errors.append(f"drafts/{f.name}：缺少 wiki 標註 → 退回 ⑥")
        for w in wikis:
            if not (ROOT / w).exists():
                errors.append(f"drafts/{f.name}：wiki 標註 {w} 不存在 → 退回 ⑥")
        allowed = set()
        for c in s["cards"]:
            if c in cards:
                for fact in cards[c][1]:
                    allowed.update(CITE.findall(fact))
        for cite in CITE.findall(body):
            if cite not in allowed:
                errors.append(f"drafts/{f.name}：出處 {cite} 不在這張投影片對應的卡片中（引用卡片以外的內容）→ 退回 ⑥")


def render_check(d):
    html = d / "index.html"
    if not html.exists():
        errors.append("index.html 不存在 → 退回 ⑧")
        return
    slides = outline_check(d)
    text = html.read_text(encoding="utf-8")
    sections = re.findall(r'<section class="slide[ "][^>]*>', text)
    if len(sections) != len(slides):
        errors.append(f"HTML 有 {len(sections)} 張，大綱有 {len(slides)} 張 → 退回 ⑧")
    for i, tag in enumerate(sections, 1):
        m = re.search(r'data-wiki="([^"]*)"', tag)
        if not m:
            errors.append(f"第 {i} 張沒有 data-wiki 標註 → 退回 ⑧")
            continue
        for w in filter(None, (x.strip() for x in m.group(1).split(","))):
            if not (ROOT / w).exists():
                errors.append(f"第 {i} 張的 Wiki 頁 {w} 不存在 → 退回 ⑥")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        errors.append("沒有安裝 playwright，無法做溢出檢查")
        return
    shots = d / "screenshots"
    shots.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 720})
        pg.goto(html.resolve().as_uri())
        n = pg.evaluate("document.querySelectorAll('section.slide').length")
        for i in range(n):
            pg.evaluate(f"window.showSlide && window.showSlide({i})")
            pg.wait_for_timeout(100)
            over = pg.evaluate(f"""(() => {{
                const s = document.querySelectorAll('section.slide')[{i}];
                const bad = [];
                if (s.scrollHeight > s.clientHeight + 1) bad.push('投影片高度溢出 ' + s.scrollHeight + '>' + s.clientHeight);
                if (s.scrollWidth > s.clientWidth + 1) bad.push('投影片寬度溢出');
                return bad; }})()""")
            for o in over:
                errors.append(f"第 {i + 1} 張：{o} → 退回 ⑥ 縮短（不在 ⑧ 硬塞）")
            pg.screenshot(path=str(shots / f"{i + 1:02d}.png"))
        b.close()


STAGES = {"coverage": coverage, "cards": cards_check, "outline": outline_check,
          "drafts": drafts_check, "render": render_check}

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in STAGES:
        print(__doc__)
        sys.exit(2)
    stage, d = sys.argv[1], (ROOT / sys.argv[2])
    STAGES[stage](d)
    print(f"check_slides {stage}：" + ("全部通過 ✅" if not errors else f"{len(errors)} 個問題 ❌"))
    for e in errors:
        print("  - " + e)
    sys.exit(1 if errors else 0)
