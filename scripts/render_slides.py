#!/usr/bin/env python3
"""⑧ 渲染 HTML：把已通過忠實度檢查的逐頁稿轉成一份 HTML 簡報。

這一關「不能改任何一個字」，所以用程式直接搬運 drafts/ 的文字，只負責排版。
用法：python3 scripts/render_slides.py slides/<主題>
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CITE = re.compile(r"\[([A-Z][A-Za-z\-]+ \d{4}, p\.\d+(?:[–-]\d+)?)\]")


def parse(f):
    t = f.read_text(encoding="utf-8")
    fm, body = {}, t
    if t.startswith("---"):
        end = t.find("\n---", 3)
        for line in t[3:end].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
        body = t[end + 4:]
    title = re.search(r"^#\s+(.+)$", body, re.M).group(1).strip()
    bullets = [l.strip()[2:] for l in body.splitlines() if l.strip().startswith("- ")]
    others = [l.strip() for l in body.splitlines()
              if l.strip() and not l.strip().startswith(("#", "- "))]
    wikis = [w.strip() for w in fm.get("wiki", "").split(",") if w.strip()]
    return title, bullets, others, wikis


def fmt(text):
    cites = CITE.findall(text)
    main = html.escape(CITE.sub("", text).strip())
    chips = "".join(f'<span class="cite">{html.escape(c)}</span>' for c in cites)
    return main, chips


def render(d):
    drafts = sorted((d / "drafts").glob("*.md"))
    total = len(drafts)
    out = []
    for i, f in enumerate(drafts, 1):
        title, bullets, others, wikis = parse(f)
        rel = [Path("../..") / w for w in wikis]
        foot = "、".join(f'<a href="{html.escape(str(r))}">{html.escape(w.replace("wiki/", ""))}</a>'
                        for w, r in zip(wikis, rel))
        attr = html.escape(", ".join(wikis))
        if i == 1:
            sub = html.escape(others[0].replace("副標：", "")) if others else ""
            out.append(f'''<section class="slide cover" data-wiki="{attr}">
  <div class="kicker">生成式人工智慧・第十週作業・LLM Wiki 教學簡報</div>
  <h1>{html.escape(title)}</h1>
  <p class="sub">{sub}</p>
  <div class="hint">按 → 或點擊右半邊翻頁</div>
</section>''')
            continue
        items = []
        for b in bullets:
            main, chips = fmt(b)
            items.append(f'<li><span class="txt">{main}</span>{chips}</li>')
        out.append(f'''<section class="slide" data-wiki="{attr}">
  <div class="num">{i:02d}<span>/ {total:02d}</span></div>
  <h2>{html.escape(title)}</h2>
  <ul>{"".join(items)}</ul>
  <footer><span class="wl">Wiki</span>{foot}</footer>
</section>''')
    page = TEMPLATE.replace("{{SLIDES}}", "\n".join(out))
    (d / "index.html").write_text(page, encoding="utf-8")
    print(f"已輸出 {d / 'index.html'}（{total} 張）")


TEMPLATE = """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI 在運動科學能做什麼？</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
:root{--bg:#EEF1EC;--paper:#FBFCF8;--ink:#14231C;--muted:#5B6B62;--accent:#1F7A4D;--accent2:#E8A33D;--line:#D5DDD6;--chip:#E6ECE6}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:var(--bg);color:var(--ink);font-family:"Noto Sans TC",system-ui,sans-serif;overflow:hidden}
#stage{position:absolute;left:50%;top:50%;width:1280px;height:720px;transform-origin:center center}
.slide{position:absolute;inset:0;width:1280px;height:720px;overflow:hidden;background:var(--paper);border-radius:18px;
  box-shadow:0 10px 40px rgba(20,35,28,.12);padding:64px 84px 96px;display:none}
.slide.active{display:block}
.slide::before{content:"";position:absolute;left:0;top:0;bottom:0;width:10px;background:var(--accent)}
.num{position:absolute;top:34px;right:48px;font-weight:900;font-size:22px;color:var(--accent)}
.num span{color:var(--muted);font-weight:500;font-size:16px;margin-left:6px}
h2{font-size:46px;font-weight:900;line-height:1.25;margin-bottom:40px;letter-spacing:.5px}
ul{list-style:none;display:flex;flex-direction:column;gap:22px}
li{font-size:28px;line-height:1.5;padding-left:34px;position:relative}
li::before{content:"";position:absolute;left:0;top:.62em;width:14px;height:14px;border-radius:4px;background:var(--accent2)}
.cite{display:inline-block;margin-left:10px;font-size:15px;font-weight:500;color:var(--muted);background:var(--chip);
  border-radius:999px;padding:2px 10px;vertical-align:middle;white-space:nowrap}
footer{position:absolute;left:84px;right:48px;bottom:30px;font-size:15px;color:var(--muted);border-top:1px solid var(--line);padding-top:12px}
footer a{color:var(--accent);text-decoration:none;margin-right:4px}
footer a:hover{text-decoration:underline}
.wl{display:inline-block;background:var(--accent);color:#fff;font-weight:700;border-radius:6px;padding:1px 8px;margin-right:10px}
.cover{background:linear-gradient(135deg,#14231C 0%,#1F4D36 100%);color:#F3F6F1;padding:120px 96px}
.cover::before{background:var(--accent2)}
.kicker{font-size:20px;letter-spacing:2px;color:#BFD8C8;margin-bottom:28px}
.cover h1{font-size:76px;font-weight:900;line-height:1.2;margin-bottom:28px}
.cover .sub{font-size:30px;color:#DDE8E0}
.hint{position:absolute;bottom:48px;left:96px;font-size:18px;color:#9FBCA9}
#bar{position:fixed;left:0;bottom:0;height:5px;background:var(--accent);transition:width .2s}
#nav{position:fixed;right:18px;bottom:16px;display:flex;gap:8px}
#nav button{border:0;background:var(--paper);color:var(--ink);font-size:18px;width:42px;height:42px;border-radius:50%;
  box-shadow:0 2px 8px rgba(0,0,0,.12);cursor:pointer}
@media (prefers-color-scheme: dark){
  :root{--bg:#0E1512;--paper:#16201B;--ink:#E7EEE9;--muted:#9AABA1;--line:#2C3A33;--chip:#22302A;--accent:#4CC38A}
}
</style>
</head>
<body>
<div id="stage">
{{SLIDES}}
</div>
<div id="bar"></div>
<div id="nav"><button id="prev" aria-label="上一張">‹</button><button id="next" aria-label="下一張">›</button></div>
<script>
const slides=[...document.querySelectorAll('section.slide')];let cur=0;
function fit(){const s=Math.min(innerWidth/1320,innerHeight/760);document.getElementById('stage').style.transform=`translate(-50%,-50%) scale(${s})`}
window.showSlide=function(i){cur=Math.max(0,Math.min(slides.length-1,i));slides.forEach((s,k)=>s.classList.toggle('active',k===cur));
  document.getElementById('bar').style.width=((cur+1)/slides.length*100)+'%';if(location.hash!=='#'+(cur+1))history.replaceState(null,'','#'+(cur+1))}
document.addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' '].includes(e.key))showSlide(cur+1);if(['ArrowLeft','PageUp'].includes(e.key))showSlide(cur-1)});
document.getElementById('next').onclick=()=>showSlide(cur+1);document.getElementById('prev').onclick=()=>showSlide(cur-1);
document.getElementById('stage').addEventListener('click',e=>{if(e.target.closest('a'))return;showSlide(cur+(e.clientX>innerWidth/2?1:-1))});
addEventListener('resize',fit);fit();showSlide((parseInt(location.hash.slice(1))||1)-1);
</script>
</body>
</html>
"""

if __name__ == "__main__":
    render(ROOT / sys.argv[1])
