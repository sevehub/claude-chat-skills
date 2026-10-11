"""Build the Claude chat skills site for GitHub Pages.
Reads skills/*.md (front matter: name, description), writes docs/.
Publish: GitHub repo > Settings > Pages > Deploy from branch > main /docs."""
import html, pathlib

SRC, OUT = pathlib.Path("skills"), pathlib.Path("docs")
(OUT / "skills").mkdir(parents=True, exist_ok=True)
(OUT / ".nojekyll").write_text("")                      # serve files as they are

def meta(text):
    head = text.split("---")[1] if text.startswith("---") else ""
    return {k.strip(): v.strip() for k, v in
            (l.split(":", 1) for l in head.splitlines() if ":" in l)}

CSS = """body{margin:0;background:#f6f0e2;color:#1b1b1b;font:15px/1.5 'IBM Plex Sans',system-ui,sans-serif}
main{max-width:46rem;margin:0 auto;padding:1.2rem}
h1{font:700 .85rem 'IBM Plex Mono',monospace;letter-spacing:.08em;text-transform:uppercase;color:#7a1f2b;margin:0 0 .4rem}
h2{font:700 1rem 'IBM Plex Mono',monospace;margin:0}
.lead{margin:0 0 1.2rem;color:#444}
section{border:1px solid #1b1b1b;border-radius:3px;background:#fff;padding:.8rem;margin-bottom:.9rem}
p{margin:.3rem 0 .6rem}
button,a.b{font:600 .78rem 'IBM Plex Mono',monospace;background:#7a1f2b;color:#f6f0e2;border:0;border-radius:3px;padding:.5rem .8rem;text-decoration:none;display:inline-block;margin-right:.4rem}
a.b.alt{background:transparent;color:#7a1f2b;border:1px solid #7a1f2b}
pre{white-space:pre-wrap;word-wrap:break-word;font:12.5px/1.5 'IBM Plex Mono',monospace;background:#faf6ec;border:1px solid #ccc;border-radius:3px;padding:.7rem;max-height:18rem;overflow:auto}
summary{cursor:pointer;font:600 .75rem 'IBM Plex Mono',monospace;color:#555}"""
JS = """function c(b){var t=b.closest('section').querySelector('pre').innerText;
(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){b.textContent='Copied'},function(){
var r=document.createRange();r.selectNodeContents(b.closest('section').querySelector('pre'));var s=getSelection();s.removeAllRanges();s.addRange(r);document.execCommand('copy');b.textContent='Copied'})}"""

cards = []
for f in sorted(SRC.glob("*.md")):
    text = f.read_text(encoding="utf-8")
    m = meta(text); name = m.get("name", f.stem)
    (OUT / "skills" / f"{name}.txt").write_text(text, encoding="utf-8")
    cards.append(f"""<section><h2>{html.escape(name)}</h2><p>{html.escape(m.get('description', ''))}</p>
<button onclick="c(this)">Copy text</button><a class="b alt" href="skills/{html.escape(name)}.txt">Open .txt</a>
<details><summary>Show text</summary><pre>{html.escape(text)}</pre></details></section>""")

(OUT / "index.html").write_text(f"""<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Claude chat skills</title>
<style>{CSS}</style><main><h1>Claude chat skills</h1>
<p class="lead">Skills for one chat only. Nothing here is installed. Paste the text into the first message of a Claude chat, or give Claude the .txt link in a chat where it can open links.</p>
{''.join(cards)}</main><script>{JS}</script></html>""", encoding="utf-8")
print(f"{len(cards)} skill(s) -> {OUT}/")
