"""Shared pieces for Sunday school lesson PDFs.

A lesson script builds a list of HTML blocks with these helpers, then calls
render() for the teacher copy and parts() for one sheet per act-out role.
Chrome headless prints the HTML to PDF.
"""
import html, json, os, re, subprocess, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(ROOT, "kjv-cache.json")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# bible-api.com serves a modernized KJV. Put his Bible's wording back.
FIXUPS = {
    ("Genesis", 3, 24): [("Cherubim,", "Cherubims,")],
}

_cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}


def verses(ref):
    """[(book, chapter, verse, text)] for a reference like 'Genesis 3:1-5'."""
    if ref not in _cache:
        url = "https://bible-api.com/" + urllib.parse.quote(ref) + "?translation=kjv"
        d = json.load(urllib.request.urlopen(url))
        _cache[ref] = {"reference": d["reference"], "verses": [
            [v["book_name"], v["chapter"], v["verse"], re.sub(r"\s+", " ", v["text"]).strip()]
            for v in d["verses"]]}
        json.dump(_cache, open(CACHE, "w"), indent=1)
    out = []
    for book, ch, vs, text in _cache[ref]["verses"]:
        for a, b in FIXUPS.get((book, ch, vs), []):
            text = text.replace(a, b)
        out.append((book, ch, vs, text.replace("’", "'")))
    return out


def esc(s):
    return html.escape(s, quote=False)


def md(s):
    """Escape, then **bold** and *italic*."""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)


def scripture(ref, label=None):
    rows = "".join(
        f'<div class="v"><span class="n">{vs}</span><span>{esc(t)}</span></div>'
        for _, _, vs, t in verses(ref))
    return f'<div class="scr"><div class="ref">{esc(label or ref)}</div>{rows}</div>'


def h(title, mins=None):
    m = f' <span class="min">{mins} min</span>' if mins else ""
    return f"<h2>{esc(title)}{m}</h2>"


def p(text):
    return f"<p>{md(text)}</p>"


def bullets(*items):
    return "<ul>" + "".join(f"<li>{md(i)}</li>" for i in items) + "</ul>"


def candy(n, question, answer):
    return (f'<div class="candy"><div class="cq">🍬 {n}. {md(question)}</div>'
            f'<div class="ca">{md(answer)}</div></div>')


def note(text):
    return f'<div class="note">{md(text)}</div>'


# An act-out is a list of ("ROLE", "line") or ("*", "stage direction").
NARRATOR = "Narrator"


def script(title, cast, lines):
    castline = " · ".join(f"<b>{esc(r)}</b> {esc(w)}" for r, w in cast)
    body = []
    for role, text in lines:
        if role == "*":
            body.append(f'<div class="dir">{md(text)}</div>')
        elif role == "#":
            body.append(f'<div class="scene">{esc(text)}</div>')
        else:
            cls = "nar" if role == NARRATOR else "role"
            body.append(f'<div class="ln {cls}"><span class="who">{esc(role)}</span>'
                        f'<span class="say">{md(text)}</span></div>')
    return (f'<div class="script"><div class="stitle">{esc(title)}</div>'
            f'<div class="cast">{castline}</div>{"".join(body)}</div>')


CSS = """
@page { size: Letter; margin: 0.55in 0.6in; }
body { font-family: -apple-system, Helvetica, Arial, sans-serif; font-size: 13.5pt;
       line-height: 1.38; color: #111; }
h1 { font-size: 24pt; margin: 0 0 2pt; }
.sub { font-size: 12pt; color: #444; margin-bottom: 10pt; }
h2 { font-size: 16pt; margin: 18pt 0 6pt; padding-bottom: 3pt;
     border-bottom: 2px solid #8a4b2a; break-after: avoid; }
.min { font-size: 11pt; color: #8a4b2a; font-weight: normal; }
p { margin: 5pt 0; }
ul { margin: 4pt 0; padding-left: 18pt; } li { margin: 3pt 0; }
.scr { background: #f4efe6; border-left: 5px solid #8a4b2a; padding: 7pt 10pt;
       margin: 8pt 0; break-inside: avoid; font-family: Georgia, serif; font-size: 14.5pt; }
.ref { font-family: -apple-system, Helvetica, sans-serif; font-weight: 700;
       font-size: 12.5pt; color: #8a4b2a; margin-bottom: 3pt; }
.v { display: flex; gap: 8pt; margin: 3pt 0; }
.n { font-weight: 700; min-width: 18pt; text-align: right; color: #8a4b2a;
     font-family: -apple-system, Helvetica, sans-serif; font-size: 12pt; padding-top: 2pt; }
.candy { border: 2.5px solid #c2185b; border-radius: 8pt; padding: 7pt 10pt;
         margin: 10pt 0; break-inside: avoid; }
.cq { font-weight: 700; font-size: 14.5pt; }
.ca { color: #444; margin-top: 3pt; }
.note { background: #eef3f8; padding: 6pt 10pt; border-radius: 6pt; margin: 8pt 0;
        break-inside: avoid; }
.script { margin: 8pt 0; }
.stitle { font-weight: 800; font-size: 15pt; }
.cast { font-size: 12pt; color: #333; margin: 2pt 0 6pt; }
.scene { font-weight: 800; margin: 10pt 0 3pt; color: #8a4b2a; break-after: avoid; }
.dir { font-style: italic; color: #555; margin: 3pt 0 3pt 92pt; }
.ln { display: flex; gap: 8pt; margin: 4pt 0; break-inside: avoid; }
.who { min-width: 84pt; font-weight: 800; font-size: 11.5pt; text-transform: uppercase;
       padding-top: 2pt; }
.ln.nar .say { font-family: Georgia, serif; font-size: 14.5pt; }
.ln.role .say { font-family: Georgia, serif; font-size: 14.5pt; font-weight: 700; }
.ln.role .who { color: #c2185b; }
.pb { break-before: page; }
/* part sheets */
.part h1 { font-size: 40pt; margin-bottom: 0; }
.part .ln .say { font-size: 20pt; }
.part .cue .say { font-size: 13pt; font-weight: normal; color: #666; font-style: italic; }
.part .cue .who { color: #999; }
.part .mine .who { color: #c2185b; font-size: 14pt; }
.part .mine .say { font-weight: 800; }
.part .dir { margin-left: 0; font-size: 14pt; }
"""


def page(title, body):
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>{esc(title)}</title>"
            f"<style>{CSS}</style></head><body>{body}</body></html>")


def to_pdf(html_text, out_pdf):
    tmp = out_pdf[:-4] + ".html"
    open(tmp, "w").write(html_text)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                    "--disable-background-networking", "--disable-component-update",
                    "--no-pdf-header-footer", f"--print-to-pdf={out_pdf}",
                    "file://" + tmp], check=True, capture_output=True)
    os.remove(tmp)


def part_sheet(lesson_title, play_title, role, how, lines):
    """One role's sheet: each of their lines with the line before it as the cue."""
    out, prev = [], None
    for who, text in lines:
        if who == "#":
            prev = None
            continue
        if who == role:
            if prev:
                pw, pt = prev
                cue = pt if len(pt) < 160 else "..." + pt[-150:]
                label = "Action" if pw == "*" else pw
                out.append(f'<div class="ln cue"><span class="who">{esc(label)}</span>'
                           f'<span class="say">{md(cue)}</span></div>')
            out.append(f'<div class="ln mine"><span class="who">YOU</span>'
                       f'<span class="say">{md(text)}</span></div><div style="height:10pt"></div>')
        prev = (who, text)
    body = (f'<div class="part"><div class="sub">{esc(lesson_title)} · {esc(play_title)}</div>'
            f"<h1>{esc(role)}</h1><p>{md(how)}</p>"
            f'<p style="color:#666;font-size:12pt">Gray is your cue. When you hear it, read the next line in big print.</p>'
            f"{''.join(out)}</div>")
    return page(role, body)
