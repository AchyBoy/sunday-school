import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from lib import *

# Built from his FINAL PLANNING NOTES (2026-11-18). Teacher copy in his voice, conversational.
TITLE = "Lesson 1.5: The Tower of Babel"
BIG = "Just because you're busy building something doesn't mean you're building what God told you to build."

# SAY / DO / ASK / EXPECTED / OPTIONAL cues (his 11-18 revision: easy to lead standing up, not a manuscript)
CUE_CSS = """<style>
p.cue { padding-left: 74pt; text-indent: -74pt; margin: 6pt 0; }
p.cue .tag { display: inline-block; width: 66pt; text-indent: 0; margin-right: 8pt; font-size: 9.5pt; font-weight: 800;
  letter-spacing: .5pt; text-align: center; border-radius: 4pt; padding: 1pt 0; color: #fff; vertical-align: 1pt; }
.t-say { background: #1565c0; } .t-do { background: #6d4c41; } .t-ask { background: #c2185b; }
.t-exp { background: #fff; color: #2e7d32 !important; border: 1.5px solid #2e7d32; }
.t-opt { background: #fff; color: #777 !important; border: 1.5px solid #aaa; }
p.cue.exp { color: #2e7d32; } p.cue.opt { color: #666; font-size: 12.5pt; }
p.cue.ask { font-weight: 700; }
.upd { background: #fff59d !important; box-shadow: 0 0 0 4px #fff59d; border-radius: 3px; }
</style>"""
def _cue(cls, tag, text):
    return f'<p class="cue {cls}"><span class="tag t-{cls}">{tag}</span>{md(text)}</p>'
def O(html):  # changed in an earlier round, no longer highlighted
    return html
def U(html):  # yellow = changed this round
    return html.replace('class="', 'class="upd ', 1)
def say(t): return _cue("say", "SAY", t)
def do(t): return _cue("do", "DO", t)
def ask(t): return _cue("ask", "ASK", t)
def exp(t): return _cue("exp", "ANSWER", t)
def opt(t): return _cue("opt", "OPTIONAL", t)

body = [
    CUE_CSS,
    f"<h1>{TITLE}</h1>",
    '<div class="sub">Genesis 11:1-9 · Series 1: In the Beginning · Ages 14-17, about 30 kids · '
    f"About 29 minutes · Big idea: <b>{esc(BIG)}</b></div>",
    '<div class="sub">Written by Andrew Young · Book: God resists the proud and arrogant</div>',
    note("**Bring:** 2 firm boards or tables (carpet) · 2 colors of plastic cups · the game timer on my phone (links page) · "
         "the rejection stickers · inspector's clipboard, pen, tape measure, fake nose and glasses · candy. "
         "**Saturday:** set up both boards and cups in the room and test the stacking. "
         "**Before class:** brief the inspector."),
    note("**Who does what (3 ladies from the girls' class):** "
         "**Lady 1 = Building Inspector** (her own sheet). "
         "**Lady 2 = Boys' station helper. Lady 3 = Girls' station helper.** They line up their team in "
         "threes and keep it moving at every buzzer. I run the timer, the lesson and the announcement."),
    note("**SAY** = how I might put it, not word for word · **DO** = action · **ASK** = question for them · "
         "**ANSWER** = the point I'm fishing for, let THEM find it · **OPTIONAL** = if there's time"),

    U(note("**Yellow = changed this round (11-21 notes, round 2).**")),
    h("Part 1. Noah, then a new group of builders", 5),
    ask("Alright, who remembers what we talked about last lesson? What did Noah build?"),
    ask("Who told him to build it?"),
    ask("After the flood, did God give Noah and his family any instructions?"),
    scripture("Genesis 9:1"),
    say("Okay, keep that in mind, because we're about to meet another group of builders."),
    scripture("Genesis 11:1-4"),
    ask("What are these people trying to build? Why do they say they want to build it?"),
    O(exp("*\"Let us make us a name, lest we be scattered abroad upon the face of the whole earth.\"*")),
    candy(1, "What did God tell Noah's family to do? And what are these people trying to avoid doing?",
          "Fill the earth (Genesis 9:1). They're trying NOT to be scattered. Let them connect the dots."),
    U(funfact("The oldest picture of Babylon's tower",
        "Babel and Babylon are the same word in Hebrew, and the Bible puts both in the land of Shinar: "
        "Babel in Genesis 11:2 and 11:9, and Babylon's king carries the temple treasures *\"into the land of "
        "Shinar\"* in Daniel 1:2. About 600 BC, King Nebuchadnezzar (the king from Daniel) had a black stone "
        "carved with HIMSELF standing next to Babylon's giant temple tower, about 300 feet tall. As far as we can "
        "tell, that tower stood where Babel was. The writing says he finished it *\"by raising its summit to "
        "the sky.\"* Sound familiar? *\"whose top may reach unto heaven.\"*",
        "**Hand a printed copy to each side.** It's worn and hard to read; the printout says so.")),

    h("Part 2. They were united", 4),
    scripture("Genesis 11:5-6"),
    funfact("They built up, God came down",
        "They built a tower *\"whose top may reach unto heaven.\"* And verse 5 says *\"the LORD came "
        "down to see\"* it. Their biggest thing ever, and God still had to come down to look at it.",
        ),
    O(say("One language, one goal, everybody pulling the same way. And it was working. Working together is a "
        "good thing! God even says nothing would stop them. But look at what they teamed up to do: God said "
        "spread out, and they were working together to stay put.")),
    ask("Have y'all ever been with a group of friends where everybody agreed to do something stupid?"),
    opt("If nobody volunteers: *\"Can somebody just 'make something up'?\"* (big air quotes) "
        "*\"We know it really happened, but we're gonna pretend you're making it up.\"*"),
    say("Just because everybody agrees doesn't mean everybody is right."),
    note("**Don't read verses 7-9 yet.** Save it for after the game."),
    say("These people had the materials, the manpower, and a plan. But how much of that depended on being "
        "able to understand each other? ...Well, we're about to find out."),

    h("Part 3. Babel Construction Company", 10),
    O(say("Alright, we're gonna play a little game. Boys against girls. It's called Babel Construction Company. "
        "**Whoever has the tallest standing tower when time's up wins.**")),
    O(do("One station each. One **foreman** + two **builders** per team, the rest line up in threes.")),
    U(say("Now, a few things you need to know. A foreman and two builders work at a time. Every 30 seconds "
        "the buzzer sounds, and you have 10 seconds to swap in the next three.")),
    say("Our official building inspector will be inspecting throughout construction. Every new foreman "
        "gets a rejection notice from her: what's wrong with your tower, and HOW you're allowed to talk "
        "until the next buzzer. Only the foreman reads it. Builders may not read rejection notices. At the end "
        "she'll do a final inspection and issue an official approval or rejection."),
    U(say("Any questions? ...Good. Because I probably wasn't going to answer them anyway. "
        "Alright, is everyone ready? ...**LET THE CONSTRUCTION BEGIN!**")),
    do("**Timer:** 2-minute game, switch every 30 seconds with a 10-second hands-off pause (screen goes red) "
       "while the next crew steps up. All one Start on my phone. "
       "**First 30 seconds:** normal talking. At every buzzer after that, the inspector hands the new foreman "
       "a REJECTED sticker. Only the foreman reads it. 2 minutes = 4 crews of 3, so run it twice if there's time "
       "and everybody gets a turn."),
    note("**Only height wins.** Her approvals and rejections don't count. Don't remind them until the end."),

    h("Part 4. Who won? Then back to Babel", 6),
    do("Time's up, everybody stops. Inspector measures both towers."),
    ask("Alright, who won?"),
    U(do("Offer a rematch, now that they know only the tallest wins.")),
    ask("Wait a minute. Is passing inspection how I said you win?"),
    ask("Then why were y'all so worried about that inspector?"),
    opt("Let them explain themselves. Have fun with it."),
    say("I told you what mattered at the very beginning. Then we started changing things. New foremen, "
        "new instructions, and this lady over here rejecting everything in sight!"),
    say("But you know what? That reminds me of something."),
    ask("Who told the people at Babel to build that tower?"),
    ask("And what had God already told Noah's family to do?"),
    say("Now watch what God does."),
    scripture("Genesis 11:7-9"),
    U(opt("Did y'all catch verse 7? They said *\"let us build\"* (verse 4). God said *\"let us go down.\"*")),
    candy(2, "Did God knock their tower down?",
          "No! The Bible never says the tower fell. Follow up: *Did they run out of bricks? Then what "
          "happened?* Their language was confused, and *\"they left off to build the city.\"*"),
    O(opt("If they ask what happened to it: the Bible doesn't say. It never says it fell, they just quit. "
        "Babylon's big tower (the one in the picture) was still there almost 300 years later, when **Alexander the Great**, "
        "who conquered most of the world, decided to rebuild it. Strabo, a Greek history writer from around the "
        "time of Jesus, says just clearing the rubble would have taken 10,000 men two months. Alexander died in Babylon in 323 BC, in Nebuchadnezzar's old "
        "palace, before it was ever rebuilt. Today, what we believe is its footprint is still in the ground in Iraq. "
        "*(History, not the Bible.)*")),
    O(ask("And what were they trying to avoid in the first place?")),
    O(exp("Being scattered.")),
    O(ask("And what happened anyway?")),
    O(exp("They got scattered.")),
    say("Isn't that something? They worked so hard to avoid the very thing God told them to do."),
    O(say("You can have a good plan, good friends, and everybody working together. But before you start "
        "building anything, talk to God about it first. Make sure it's the direction He wants you to go.")),

    h("Part 5. Pride, and asking God first", 4),
    scripture("James 4:6"),
    say("Pride isn't always bragging or thinking you're better than everybody. Sometimes pride sounds like: "
        "*\"I know what I'm doing.\" \"I don't need advice.\" \"I've got this figured out.\" "
        "\"I don't need to ask God about this.\"*"),
    say("Being confident isn't the problem. Trusting my own judgment and ignoring God's direction is."),
    scripture("Proverbs 3:5-6"),
    candy(3, "Have you ever gotten so focused on doing something that you forgot to ask whether it was "
             "the right thing to do?",
          "Anyone who shares gets candy. Don't push if nobody does."),
    say("Last lesson, Noah built because God told him to. This lesson, the people at Babel built to make a name "
        "for themselves. Both had plans. Both were builders. Both worked toward a goal. But only one was "
        "following God's instructions."),
    O(scripture("Psalm 127:1")),
    p(f"**{BIG}**"),

    h("Extra fun facts, if they ask"),
    opt("**\"Babble\" doesn't come from \"Babel.\"** Everybody thinks so, but the English word just imitates baby talk."),
]

# ---- the inspector's sheet (a teacher plays her) ----
INSPECTOR = [
    "<h1>Building Inspector</h1>",
    f'<div class="sub">{TITLE} · Babel Construction Company</div>',
    p("**Who you are:** an overly serious government inspector. Your job is VERY important "
      "and you have no idea how ridiculous you are."),
    p("**Props:** clipboard, pen for extremely serious notes, tape measure, fake nose and glasses, "
      "the REJECTED stickers, APPROVED and REJECTED signs."),
    note("**The secret:** only HEIGHT wins. Your approvals and rejections don't count at all. "
         "Don't tell them. Never stop the game, keep walking around while they build."),
    "<h2>While they build</h2>",
    bullets("\"Is that a load-bearing cup?\"",
            "\"Where are your permits?\"",
            "\"That doorway is not ADA compliant.\"",
            "\"I'm seeing a concerning amount of confidence for a structure with no foundation.\"",
            "\"Who approved this?\"",
            "\"I'm not saying it's going to fall. I'm saying I wouldn't stand next to it.\"",
            "\"I've seen better construction from a toddler with mashed potatoes.\""),
    p("**Tape measure bit:** measure something holding the tape wrong, study it very seriously, then: "
      "*\"According to my calculations, this doorway is approximately... seventeen.\"* "
      "Write it on the clipboard and walk away."),
    "<h2>Every buzzer: a new foreman, a new rejection</h2>",
    p("First 30 seconds, no stickers. Then at every buzzer, hand each team's NEW foreman a REJECTED sticker. "
      "It says what to fix and how they're allowed to talk. Only the foreman reads it. Make a show of it: "
      "adjust your glasses, concerned noises, *\"Mmmmm. No. No, no, no. Oh dear.\"*"),
    p("If they haven't fixed it when you come back around: *\"Still rejected!\"*"),
    "<h2>Final inspection</h2>",
    p("Look at both towers: the other-color cups, how it looks, whatever concern you invent. "
      "When time's up, measure both towers. Then judge them your way, APPROVED or REJECTED, no script. "
      "Andrew may offer a rematch."),
    p("**If your favorite lost:** *\"EXCUSE ME?!\"* ... Andrew: *\"The rules said tallest tower wins.\"* "
      "... You: *\"Well, that's a terrible system.\"*"),
    p("**Optional, if it fits:** *\"These towers are impressive, but I have one question... "
      "WHO AUTHORIZED THIS CONSTRUCTION?\"*"),
]


# ---- station helper sheet (2 of the ladies, one per team) ----
HELPER = [
    "<h1>Station Helper</h1>",
    f'<div class="sub">{TITLE} · Babel Construction Company · one helper at the boys\' station, one at the girls\'</div>',
    p("**Your job:** keep your team's line moving. Andrew runs the lesson; "
      "the inspector does the funny part. You keep the game running."),
    note("**The secret:** only HEIGHT wins. The inspector's rejections don't count. Don't tell them."),
    "<h2>Before the game</h2>",
    bullets("Andrew sets up both stations Saturday: a firm board, your team's cup color, a few of the other color nearby.",
            "When Andrew starts the game, line your team up in groups of 3: a foreman and two builders."),
    "<h2>During the game</h2>",
    bullets("Andrew runs the timer. It buzzes every 30 seconds; the game is 2 minutes.",
            "**First 30 seconds:** normal talking.",
            "**Every buzzer:** the 3 at the tower step out, the next 3 step in. The inspector hands the new "
            "foreman a rejection sticker. Only the foreman reads it, cover it if a builder peeks.",
            "2 minutes = 4 crews. Andrew may run it twice so everyone gets a turn."),
    "<h2>When time is up</h2>",
    p("Everybody hands off, nobody touches the tower. The inspector measures. Andrew takes it from there."),
]

# ---- cards to print and cut ----
# Each sticker = what to fix + how the foreman may talk (his 11-20 simplification).
STICKERS = [
    ("Bottom row needs 1 cup of the other team's color.", "Speak only in questions."),
    ("Row 2 needs 1 cup of the other team's color.", "Sing every instruction."),
    ("Row 3 needs 2 cups of the other team's color.", "Say your words in reverse order."),
    ("Bottom row needs 2 cups of the other team's color.", "Only three words at a time."),
    ("Row 4 needs 2 cups of the other team's color.", "Whisper every instruction."),
    ("Row 2 needs 2 cups of the other team's color.", "Talk like a robot."),
    ("Row 3 needs 1 cup of the other team's color.", "Narrate like a sports announcer."),
    ("Top cup must be the other team's color.", "Say everything dramatically."),
    ("Row 5 needs 2 cups of the other team's color.", "Only say yes, no, or maybe."),
    ("Bottom row needs 3 cups of the other team's color.", "Quote a Bible verse every time."),
]
CARD_CSS = """
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }
.card { border: 1.5px dashed #888; height: 1.8in; padding: 8pt 10pt; overflow: hidden; box-sizing: border-box;
        display: flex; flex-direction: column; justify-content: center; text-align: center; }
.card .k { font-size: 10pt; letter-spacing: 1pt; color: #8a4b2a; font-weight: 800; }
.card .t { font-size: 21pt; font-weight: 800; margin-top: 6pt; }
.card .s { font-size: 10pt; color: #666; margin-top: 6pt; }
.rej { border: 4px solid #b71c1c; padding: 18pt; margin: 0 0 22pt; text-align: center; break-inside: avoid; }
.rej .d { font-weight: 800; letter-spacing: 2pt; }
.rej .big { font-size: 34pt; font-weight: 900; color: #b71c1c; margin: 6pt 0; }
.rej .v { font-weight: 700; }
.rej .body { font-size: 17pt; margin: 12pt 0; }
.stamp { height: 3.8in; display: flex; align-items: center; justify-content: center;
         font-size: 72pt; font-weight: 900; border: 8px solid; margin-bottom: 0.3in; }
"""
cards = "".join(
    f'<div class="card"><div class="k" style="color:#b71c1c;font-size:13pt;letter-spacing:2pt">REJECTED</div><div class="s" style="margin-top:0">Violation #11-{n+1} · <b>foreman only</b></div>'
    f'<div class="s" style="font-size:12pt;color:#111;margin-top:4pt;font-weight:600">{esc(fix)}</div>'
    f'<div class="k" style="margin-top:6pt;font-size:8pt">UNTIL THE NEXT BUZZER, THE FOREMAN MUST:</div>'
    f'<div class="t" style="font-size:15pt;margin-top:1pt">{esc(talk)}</div>'
    f'</div>'
    for n, (fix, talk) in enumerate(STICKERS))
PRINT = (f"<style>{CARD_CSS}</style>"
         '<div class="sub">REJECTED stickers: print on full-sheet sticker paper (or plain paper) and cut on '
         'the dashed lines. 2 pages = one set per team.</div>'
         f'<div class="grid">{cards}</div><div class="pb"></div><div class="grid">{cards}</div>'
         '<div class="pb"></div><div class="stamp" style="color:#2e7d32;border-color:#2e7d32">APPROVED</div>'
         '<div class="stamp" style="color:#2e7d32;border-color:#2e7d32">APPROVED</div>'
         '<div class="pb"></div><div class="stamp" style="color:#b71c1c;border-color:#b71c1c">REJECTED</div>'
         '<div class="stamp" style="color:#b71c1c;border-color:#b71c1c">REJECTED</div>')

out = os.path.join(HERE, "pdf")
os.makedirs(out, exist_ok=True)
for f in os.listdir(out):
    os.remove(os.path.join(out, f))
to_pdf(page(TITLE, "".join(body)), os.path.join(out, "1.5 Teacher - The Tower of Babel.pdf"))
to_pdf(page("Inspector", "".join(INSPECTOR)), os.path.join(out, "Part - Inspector.pdf"))
to_pdf(page("Station Helper", "".join(HELPER)), os.path.join(out, "Part - Station helper.pdf"))
to_pdf(page("Cards to print", PRINT), os.path.join(out, "Part - Cards to print.pdf"))
import subprocess; subprocess.run([sys.executable, os.path.join(HERE, "stele.py")], check=True)  # wiped above, rebuild
FINAL = False
open(os.path.join(HERE, "index.html"), "w").write(web_page(
    os.path.basename(HERE), TITLE, "".join(body),
    ["Part - Inspector.pdf", "Part - Station helper.pdf", "Part - Cards to print.pdf", "Part - Picture of the tower (print).pdf"], final=FINAL))
mark = os.path.join(HERE, "FINAL")
if FINAL:
    open(mark, "w").close()
elif os.path.exists(mark):
    os.remove(mark)
print("done")
