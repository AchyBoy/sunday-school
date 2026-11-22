"""One-page printout: the Tower of Babel Stele (Schøyen MS 2063), labeled for the class."""
import os, sys, base64
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from lib import page, to_pdf

img = base64.b64encode(open(os.path.join(HERE, "img", "stele.jpg"), "rb").read()).decode()
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
    <h1>The oldest picture of Babylon's tower</h1>
    <div class="when">Black stone · about 600 BC · 2,600 years old</div>
    <p><b>It's worn and hard to see after 2,600 years.</b> Look for the king's tall pointed hat at the top right.</p>
    <p>Carved for <b>King Nebuchadnezzar</b>, the king from the book of Daniel. He stands on the right.
       Next to him is Babylon's giant temple tower, drawn in steps, about 300 feet tall.</p>
    <p>The writing says he finished the tower</p>
    <p class="q">"by raising its summit to the sky."</p>
    <p>Sound familiar? Genesis 11:4:</p>
    <p class="q">"let us build us a city and a tower, whose top may reach unto heaven"</p>
    <p>Babel and Babylon are the same word in the Bible, in the same land, Shinar. Many people think this
       tower stood where Babel was. Nobody can prove it was the same tower.</p>
    <div class="cr">The Tower of Babel Stele, MS 2063. Photo &copy; The Sch&oslash;yen Collection, Oslo and London,
       photo Tom Jensen. Printed for one Sunday school class.</div>
  </div>
</div>"""
out = os.path.join(HERE, "pdf")
os.makedirs(out, exist_ok=True)
to_pdf(page("Tower of Babel Stele", body), os.path.join(out, "Part - Picture of the tower (print).pdf"))
print("stele done")
