"""One-page printout: the Tower of Babel Stele (Schøyen MS 2063), labeled for the class."""
import os, sys, base64
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from lib import page, to_pdf

img = base64.b64encode(open(os.path.join(HERE, "img", "stele.jpg"), "rb").read()).decode()
foot = base64.b64encode(open(os.path.join(HERE, "img", "footprint.jpg"), "rb").read()).decode()
plan = base64.b64encode(open(os.path.join(HERE, "img", "plan.png"), "rb").read()).decode()
CSS = """
@page { size: Letter; margin: 0.45in 0.55in; }
.wrap { display: flex; gap: 18pt; align-items: flex-start; }
.ph { position: relative; width: 4.1in; flex: none; }
.ph img { width: 100%; display: block; border-radius: 4pt; }
.tag { position: absolute; background: #fff; color: #111; font: 800 11.5pt -apple-system, Helvetica, sans-serif;
       padding: 3pt 7pt; border-radius: 5pt; border: 2.5px solid #c2185b; white-space: nowrap; }
.dot { position: absolute; width: 16pt; height: 16pt; border: 3px solid #ffeb3b; border-radius: 50%; }
.side { font-size: 13pt; }
.side h1 { font-size: 26pt; line-height: 1.1; margin: 0 0 6pt; }
.side .when { color: #8a4b2a; font-weight: 700; margin-bottom: 10pt; }
.side p { margin: 0 0 9pt; }
.q { border-left: 4px solid #8a4b2a; padding: 4pt 9pt; background: #f4efe6; font-family: Georgia, serif; }
.cr { font-size: 8.5pt; color: #777; margin-top: 10pt; }
"""
body = f"""<style>{CSS}</style>
<div class="wrap">
  <div class="ph">
    <img src="data:image/jpeg;base64,{img}">
    <div class="dot" style="left:69%;top:9%"></div>
    <div class="tag" style="left:40%;top:2%">The king &rarr;</div>
    <div class="tag" style="left:6%;top:15%">the tower, in steps (faint) &darr;</div>
    <div class="tag" style="left:30%;top:80%">writing &darr;</div>
  </div>
  <div class="side">
    <h1>A picture of Babylon's tower</h1>
    <div class="when">Black stone · historians believe about 2,600 years old</div>
    <p><b>It's old, worn and hard to see.</b> Look for the king's tall pointed hat at the top right.</p>
    <p>Historians believe it was carved for <b>King Nebuchadnezzar</b>, the king from the book of Daniel. He stands
       on the right, next to Babylon's giant temple tower. They believe it stood 200 to 300 feet tall.</p>
    <p>In the museum's translation, he says he finished it</p>
    <p class="q">"by raising its summit to the sky."</p>
    <p>Sound familiar? Genesis 11:4:</p>
    <p class="q">"let us build us a city and a tower, whose top may reach unto heaven"</p>
    <p>Babel and Babylon are the same word in Hebrew, in the same land, Shinar. Many historians believe this
       tower is tied to the Tower of Babel.</p>
    <div class="cr">The Tower of Babel Stele, MS 2063. Photo &copy; The Sch&oslash;yen Collection, Oslo and London,
       photo Tom Jensen. Printed for one Sunday school class.</div>
  </div>
</div>
<div style="break-before:page"></div>
<h1 style="font-size:26pt;margin:0 0 4pt">What's left of it today</h1>
<p style="font-size:14pt;margin:0 0 10pt">In Iraq, about 55 miles south of Baghdad. Historians believe this is part of the tower's base,
 now filled with water and reeds.</p>
<img src="data:image/jpeg;base64,{foot}" style="width:100%;border-radius:4pt">
<div style="display:flex;gap:16pt;margin-top:12pt;align-items:center;break-inside:avoid">
  <div style="position:relative;width:2.7in;flex:none"><img src="data:image/png;base64,{plan}" style="width:100%;display:block;border:1px solid #999">
    <div style="position:absolute;left:18%;top:35%;width:26%;height:21%;border:4px solid #c2185b;border-radius:50%"></div></div>
  <div style="font-size:15pt"><p style="margin:0 0 9pt"><b>From above:</b> archaeologists dug here about 100 years ago and drew this map.
    Historians believe the circled square is where the tower stood, about 300 feet on each side.</p>
    <p style="margin:0">Alexander the Great wanted to rebuild it. He died in Babylon first, and it was never rebuilt.</p></div>
</div>
<div class="cr">Photo: Marjon Verburg, CC0. Plan: Robert Koldewey, public domain. Both from Wikimedia Commons.</div>"""
out = os.path.join(HERE, "pdf")
os.makedirs(out, exist_ok=True)
to_pdf(page("Tower of Babel Stele", body), os.path.join(out, "Part - Picture of the tower (print).pdf"))
print("stele done")
