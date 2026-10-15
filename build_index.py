"""Writes index.html: every lesson, newest first, teacher copy + part sheets."""
import os, urllib.parse
from lib import esc

ROOT = os.path.dirname(os.path.abspath(__file__))
VERSION = "1.1"

cards = []
for d in sorted(os.listdir(os.path.join(ROOT, "lessons")), reverse=True):
    pdf = os.path.join(ROOT, "lessons", d, "pdf")
    if not os.path.isdir(pdf):
        continue
    files = sorted(os.listdir(pdf))
    teacher = [f for f in files if not f.startswith("Part - ") and f.endswith(".pdf")]
    parts = [f for f in files if f.startswith("Part - ")]
    href = lambda f: urllib.parse.quote(f"lessons/{d}/pdf/{f}")
    title = esc(teacher[0][:-4].replace(" Teacher - ", ": ") if teacher else d)
    t = "".join(f'<a class="big" href="{href(f)}">📖 Teacher copy</a>' for f in teacher)
    # Until he signs a lesson off, the web copy (with ✎ notes) comes first and the PDF is second.
    if os.path.exists(os.path.join(ROOT, "lessons", d, "index.html")) and \
            not os.path.exists(os.path.join(ROOT, "lessons", d, "FINAL")):
        title += ' <span class="draft">DRAFT</span>'
        t = (f'<a class="big" href="lessons/{d}/">✎ Read and mark up</a>'
             + "".join(f'<a class="sec" href="{href(f)}">PDF teacher copy</a>' for f in teacher))
    p = "".join(f'<a class="part" href="{href(f)}">{esc(f[7:-4])}</a>' for f in parts)
    cards.append(f'<section><h2>{title}</h2>{t}'
                 + (f'<div class="lbl">Act-out parts</div><div class="parts">{p}</div>' if p else "")
                 + "</section>")

open(os.path.join(ROOT, "index.html"), "w").write(f"""<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><meta name="x-ss-version" content="{VERSION}">
<title>Sunday School Lessons</title><style>
body{{font-family:-apple-system,Helvetica,sans-serif;margin:0;background:#f6f2ea;color:#111}}
header{{background:#8a4b2a;color:#fff;padding:18px 16px}} h1{{margin:0;font-size:24px}}
main{{padding:12px;max-width:640px;margin:auto}}
section{{background:#fff;border-radius:14px;padding:14px;margin:12px 0;box-shadow:0 1px 3px #0002}}
h2{{margin:0 0 10px;font-size:19px}}
a{{text-decoration:none;color:inherit}}
.big{{display:block;background:#8a4b2a;color:#fff;font-weight:700;font-size:18px;padding:14px;border-radius:10px;text-align:center}}
.sec{{display:block;text-align:center;padding:10px;margin-top:8px;color:#8a4b2a;font-weight:600}}
.draft{{font-size:12px;background:#8a4b2a;color:#fff;border-radius:5px;padding:2px 6px;vertical-align:3px}}
.lbl{{margin:14px 0 6px;font-size:13px;color:#666;text-transform:uppercase;font-weight:700}}
.parts{{display:flex;flex-wrap:wrap;gap:8px}}
.part{{background:#f4efe6;border:1px solid #d9c7b2;padding:10px 12px;border-radius:9px;font-weight:600}}
@media (prefers-color-scheme:dark){{body{{background:#1b1714;color:#eee}}section{{background:#2a2420}}
.part{{background:#3a302a;border-color:#5a4a3e}}.sec{{display:block;text-align:center;padding:10px;margin-top:8px;color:#8a4b2a;font-weight:600}}
.draft{{font-size:12px;background:#8a4b2a;color:#fff;border-radius:5px;padding:2px 6px;vertical-align:3px}}
.lbl{{color:#aaa}}}}
</style></head><body><header><h1>Sunday School Lessons</h1></header>
<main>{"".join(cards)}</main></body></html>""")
print("index:", len(cards), "lessons")
