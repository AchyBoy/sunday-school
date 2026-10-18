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


_READ = set()


def scripture(ref, label=None):
    # A verse printed a second time is marked so no student is picked to read it again.
    if ref in _READ:
        label = f"{label or ref} · already read, I'll say it"
    _READ.add(ref)
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


def funfact(title, *parts):
    """The lesser known fact box, one per lesson. parts are paragraphs (md)."""
    # a part that is a list is printed as lines under each other
    body = "".join(f"<p>{'<br>'.join(md(y) for y in x)}</p>" if isinstance(x, list)
                   else f"<p>{md(x)}</p>" for x in parts)
    return f'<div class="fun"><div class="ft">⭐ Fun fact: {md(title)}</div>{body}</div>'


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
.fun { border: 2.5px solid #e0a100; background: #fff8e1; border-radius: 8pt;
       padding: 7pt 10pt; margin: 10pt 0; break-inside: avoid; }
.fun .ft { font-weight: 800; font-size: 14.5pt; margin-bottom: 3pt; }
.fun p { margin: 4pt 0; }
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


# ---- web copy: the teacher copy as a page that looks like the PDF, with ✎ notes ----
# Notes go to the same store as the book's (api.jobhubgo.com/api/yam/<key>-ss). The key is
# never in this repo: the page reads it from ?c=<key>, or from the book site's saved key
# (same origin, achyboy.github.io), so his phone already has it. No key = no pencils.
WEB_JS = r"""
const API = "https://api.jobhubgo.com/api/yam/";
const LESSON = document.body.dataset.lesson, BUILD = Number(document.body.dataset.build);
function lsGet(k) { try { return JSON.parse(localStorage.getItem(k)); } catch { return null; } }
(function () { const k = new URLSearchParams(location.search).get("c");
  if (k) localStorage.setItem("ss.ckey", JSON.stringify(k)); })();
const BASE = lsGet("ss.ckey") || lsGet("wyl.ckey");
const CKEY = BASE ? BASE + "-ss" : null;
const $ = (id) => document.getElementById(id);
let comments = [];
const TARGETS = ".doc h1, .doc .sub, .doc h2, .doc p, .doc li, .doc .note, .doc .candy, .doc .fun, .doc .scr .ref, .doc .scr .v, .doc .stitle, .doc .cast, .doc .scene, .doc .dir, .doc .ln";
const mineAt = (i) => comments.filter(c => c.lesson === LESSON && c.i === i);
async function load() {
  try { const j = await (await fetch(API + CKEY)).json(); comments = (j.data && j.data.comments) || []; } catch {}
  mark();
}
async function save(mutate) {
  for (let n = 0; n < 2; n++) {
    let cur = [];
    try { const j = await (await fetch(API + CKEY)).json(); cur = (j.data && j.data.comments) || []; } catch {}
    const next = mutate(cur.slice());
    try {
      const r = await fetch(API + CKEY, { method: "PUT", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: { comments: next }, updatedAt: Date.now() }) });
      if ((await r.json()).ok) { comments = next; mark(); return true; }
    } catch {}
  }
  return false;
}
function mark() {
  document.querySelectorAll(".pen").forEach(b => b.classList.toggle("has", mineAt(Number(b.dataset.i)).length > 0));
  const n = comments.filter(c => c.lesson === LESSON).length;
  $("count").textContent = n ? n + " note" + (n > 1 ? "s" : "") + " on this lesson" : "";
}
let at = null;
function renderOld() {
  const mine = mineAt(at.i);
  $("cmtOld").innerHTML = mine.map(c => `<div class="old"><span></span><button data-id="${c.id}">Delete</button></div>`).join("");
  $("cmtOld").querySelectorAll(".old span").forEach((el, k) => el.textContent = mine[k].text);
  $("cmtOld").querySelectorAll("button").forEach(b => b.onclick = async () => {
    $("cmtStatus").textContent = "Deleting...";
    await save(cur => cur.filter(c => c.id !== b.dataset.id));
    $("cmtStatus").textContent = ""; renderOld();
  });
}
function open(i, text) {
  at = { i, quote: text.slice(0, 80) };
  $("cmtQuote").textContent = "“" + text.slice(0, 90) + (text.length > 90 ? "...”" : "”");
  $("cmtText").value = ""; $("cmtStatus").textContent = "";
  renderOld(); $("cmt").classList.add("open"); $("cmtText").focus();
}
$("cmtClose").onclick = () => $("cmt").classList.remove("open");
$("cmtSave").onclick = async () => {
  const text = $("cmtText").value.trim();
  if (!text) return;
  $("cmtStatus").textContent = "Saving...";
  const c = { id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6), lesson: LESSON, i: at.i,
              quote: at.quote, text, at: new Date().toISOString(), v: BUILD };
  if (await save(cur => cur.concat([c]))) { $("cmtText").value = ""; $("cmtStatus").textContent = "Saved"; renderOld(); }
  else $("cmtStatus").textContent = "Didn't save, try again";
};
if (CKEY) {
  document.body.classList.add("editing");
  document.querySelectorAll(TARGETS).forEach((el, i) => {
    const text = el.textContent.trim();
    const b = document.createElement("button");
    b.className = "pen"; b.textContent = "✎"; b.dataset.i = i;
    b.setAttribute("aria-label", "Note on this");
    b.onclick = (e) => { e.stopPropagation(); open(i, text); };
    el.appendChild(b);
  });
  load();
}
"""

WEB_CSS = """
html { background: #d9d4cc; }
body { margin: 0; padding: 0 0 40vh; }
.top { position: sticky; top: 0; z-index: 5; background: #8a4b2a; color: #fff; font: 600 14px -apple-system, Helvetica, sans-serif;
       padding: 10px 14px; display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
.top a { color: #fff; } .top .draft { background: #fff; color: #8a4b2a; border-radius: 5px; padding: 2px 7px; font-weight: 800; }
.top #count { margin-left: auto; opacity: .9; }
.doc { background: #fff; max-width: 7.3in; margin: 14px auto; padding: 0.55in 0.6in; box-shadow: 0 2px 10px #0003; }
@media (max-width: 600px) { .doc { margin: 0; padding: 18px 14px; font-size: 12pt; } .who { min-width: 64pt; } .dir { margin-left: 0; } }
.parts { max-width: 7.3in; margin: 14px auto; font: 15px -apple-system, Helvetica, sans-serif; padding: 0 10px; }
.parts a { display: inline-block; background: #fff; border: 1px solid #b9a58e; border-radius: 8px; padding: 8px 11px; margin: 4px 4px 0 0;
           color: #111; text-decoration: none; font-weight: 600; }
.pen { display: none; border: 0; background: none; font-size: 15px; color: #8a4b2a; opacity: .45; padding: 0 5px; cursor: pointer;
       font-family: -apple-system, sans-serif; font-weight: normal; vertical-align: baseline; }
.editing .pen { display: inline; } .pen.has { opacity: 1; color: #c2185b; font-weight: 800; }
.v .pen, .ln .pen { align-self: flex-start; }
.cmt { position: fixed; inset: auto 0 0 0; z-index: 60; background: #fff; border-top: 1px solid #ccc; display: none;
       padding: 16px 18px calc(env(safe-area-inset-bottom) + 16px); font: 16px -apple-system, Helvetica, sans-serif;
       box-shadow: 0 -10px 30px rgba(0,0,0,.2); max-height: 75vh; overflow: auto; }
.cmt.open { display: block; }
.cmt .quote { color: #666; font-style: italic; margin-bottom: 10px; }
.cmt .old { border-left: 3px solid #c2185b; padding: 4px 10px; margin: 8px 0; display: flex; gap: 10px; justify-content: space-between; }
.cmt .old button, .cmt .acts button { border: 0; background: none; font: inherit; color: #666; }
.cmt textarea { width: 100%; box-sizing: border-box; min-height: 90px; font: inherit; border: 1px solid #ccc; border-radius: 8px; padding: 8px; }
.cmt .acts { display: flex; align-items: center; gap: 10px; margin-top: 8px; }
.cmt .acts .status { flex: 1; color: #666; }
.cmt .acts .save { background: #8a4b2a; color: #fff; border-radius: 8px; padding: 8px 18px; font-weight: 700; }
"""


# Always the newest on reload (same as the coffee site). GitHub Pages caches a page up to
# 10 minutes at its CDN, so after a deploy a reload can still show the old one. version.json
# is fetched with a unique URL (never cached); if it names a newer build than this page, hop
# once to ?v=<build>, a URL the cache has never seen. deploy.sh stamps SITE_BUILD in every
# page, every .pdf?v= link and version.json together.
FRESH = """<script>var SITE_BUILD='dev';
(function(){
  if(location.protocol==='file:'||SITE_BUILD==='dev') return;
  fetch('/sunday-school/version.json?t='+Date.now(),{cache:'no-store'}).then(function(r){return r.json()}).then(function(j){
    if(!j||!j.build||j.build===SITE_BUILD) return;
    var k='ss-fresh-'+j.build; try{ if(sessionStorage.getItem(k)) return; sessionStorage.setItem(k,'1'); }catch(e){}
    var u=new URL(location.href); u.searchParams.set('v',j.build); location.replace(u.toString());
  }).catch(function(){});
})();
</script>"""


def web_page(lesson_id, title, body, parts=(), final=False):
    """lessons/<id>/index.html: the teacher copy on screen, same styles as the PDF, ✎ on every block."""
    import time
    tag = "" if final else '<span class="draft">DRAFT</span>'
    plinks = "".join(f'<a href="pdf/{urllib.parse.quote(f)}">{esc(f[7:-4])}</a>' for f in parts)
    return (f"<!doctype html><html><head><meta charset='utf-8'>"
            f"<meta name='viewport' content='width=device-width,initial-scale=1'><meta name='robots' content='noindex'>"
            f"{FRESH}"
            f"<title>{esc(title)}</title><style>{CSS}{WEB_CSS}</style></head>"
            f"<body data-lesson='{esc(lesson_id)}' data-build='{int(time.time())}'>"
            f"<div class='top'><a href='../../'>&larr; Lessons</a>{tag}<span id='count'></span></div>"
            f"<div class='doc'>{body}</div>"
            + (f"<div class='parts'><b>Act-out part sheets (PDF)</b><br>{plinks}</div>" if plinks else "")
            + "<div class='cmt' id='cmt'><div class='quote' id='cmtQuote'></div><div id='cmtOld'></div>"
              "<textarea id='cmtText' placeholder='Your edit or note on this part'></textarea>"
              "<div class='acts'><button id='cmtClose'>Close</button><span class='status' id='cmtStatus'></span>"
              "<button class='save' id='cmtSave'>Save</button></div></div>"
            f"<script>{WEB_JS}</script></body></html>")
