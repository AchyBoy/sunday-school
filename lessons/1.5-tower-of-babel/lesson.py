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
</style>"""
def _cue(cls, tag, text):
    return f'<p class="cue {cls}"><span class="tag t-{cls}">{tag}</span>{md(text)}</p>'
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
    note("**Bring:** 2 firm boards or tables (carpet) · 2 colors of plastic cups · 30-second timer · "
         "the printed cards · inspector's clipboard, pen, tape measure, fake nose and glasses · candy. "
         "**Before class:** test the cups on the boards, brief the inspector, agree when she does the rejection."),
    note("**Who does what (3 ladies from the girls' class):** "
         "**Lady 1 = Building Inspector** (her own sheet). "
         "**Lady 2 = Boys' station helper**, also runs the 30-second buzzer. "
         "**Lady 3 = Girls' station helper.** Helpers line up their team in threes, hand each new foreman "
         "a card, and keep builders from reading cards. I run the lesson and the announcement."),
    note("**SAY** = how I might put it, not word for word · **DO** = action · **ASK** = question for them · "
         "**ANSWER** = the point I'm fishing for, let THEM find it · **OPTIONAL** = if there's time"),

    h("Part 1. Noah, then a new group of builders", 5),
    do("A few boys quietly set up the two building stations while we talk."),
    ask("Alright, who remembers what we talked about last week? What did Noah build?"),
    ask("Who told him to build it?"),
    ask("After the flood, did God give Noah and his family any instructions?"),
    scripture("Genesis 9:1"),
    say("Okay, keep that in mind, because we're about to meet another group of builders."),
    scripture("Genesis 11:1-4"),
    ask("What are these people trying to build? Why do they say they want to build it?"),
    exp("*\"Let us make us a name.\"*"),
    candy(1, "What did God tell Noah's family to do? And what are these people trying to avoid doing?",
          "Fill the earth (Genesis 9:1). They're trying NOT to be scattered. Let them connect the dots."),
    opt("Fun fact: Babel and Babylon are the same word in the Bible. Centuries later King Nebuchadnezzar "
        "rebuilt Babylon and stamped HIS NAME into the bricks; museums have them today. *(A connection, "
        "not something Genesis says: the bricks are from long after the tower.)*"),

    h("Part 2. They were united", 4),
    scripture("Genesis 11:5-6"),
    funfact("They built up, God came down",
        "They built a tower *\"whose top may reach unto heaven.\"* And verse 5 says *\"the LORD came "
        "down to see\"* it. Their biggest thing ever, and God still had to come down to look at it.",
        "*If they want more:* their words are *\"Go to, let us...\"* (verses 3 and 4). God answers "
        "with their own words in verse 7: *\"Go to, let us go down.\"*"),
    say("One language, one goal, everybody working together, and it was working. "
        "The problem wasn't the teamwork. It was what they were building."),
    ask("Have y'all ever been with a group of friends where everybody agreed to do something stupid?"),
    say("Just because everybody agrees doesn't mean everybody is right."),
    note("**Don't read verses 7-9 yet.** Save it for after the game."),
    say("These people had the materials, the manpower, and a plan. But how much of that depended on being "
        "able to understand each other? ...Well, we're about to find out."),

    h("Part 3. Babel Construction Company", 10),
    do("Boys vs. girls, one station each. One **foreman** + two **builders** per team. Buzzer every "
       "**30 seconds**, all three rotate out. Five rotations = everyone once; go around twice if we can."),
    do("Read the announcement. Say the scoring rule FIRST, then bury it under all the inspection rules."),
    say("Welcome to Babel Construction Company! Each team will build the tallest tower possible with the "
        "materials provided. **THE WINNER WILL BE DETERMINED BY THE FINAL HEIGHT OF THEIR STANDING TOWER.**"),
    say("Now, a few things you need to know. A foreman and two builders work at a time. Every 30 seconds "
        "the buzzer sounds and all three get replaced. Each new foreman gets a special communication "
        "instruction that must be followed at all times."),
    say("Our official building inspector will be inspecting throughout construction. She has the authority "
        "to issue rejection notices, require modifications, and demand immediate corrections. All rejection "
        "notices must be communicated by the foreman to the builders. Builders may not read them. At the end "
        "she'll do a final inspection and issue an official approval or rejection."),
    say("Any questions? ...Good. Because I probably wasn't going to answer them anyway. "
        "**LET THE CONSTRUCTION BEGIN!**"),
    do("**First 30 seconds:** normal talking. After the first buzzer, every new foreman gets a secret card. "
       "Only the foreman reads it."),
    do("The inspector roams, never stops the game. **About halfway** she fails BOTH towers and hands each "
       "foreman a rejection notice (5 cups of the other team's color in rows 3-5). It passes to the next foreman."),
    note("**Only height wins.** Her approvals and rejections don't count. Don't remind them until the end."),

    h("Part 4. Who won? Then back to Babel", 6),
    do("Time's up, everybody stops. Inspector measures both towers."),
    ask("Alright, who won?"),
    ask("Now, who passed inspection?"),
    do("Inspector announces APPROVED / REJECTED for each, very seriously."),
    ask("Wait a minute. Is passing inspection how I said you win?"),
    ask("Then why were y'all so worried about that inspector?"),
    opt("Let them explain themselves. Have fun with it."),
    say("I told you what mattered at the very beginning. Then we started changing things. New foremen, "
        "new instructions, and this lady over here rejecting everything in sight!"),
    do("Inspector: *\"And I'd do it again.\"*"),
    say("But you know what? That reminds me of something."),
    ask("Who told the people at Babel to build that tower?"),
    ask("And what had God already told Noah's family to do?"),
    say("Now watch what God does."),
    scripture("Genesis 11:7-9"),
    candy(2, "Did God knock their tower down?",
          "No! The Bible never says the tower fell. Follow up: *Did they run out of bricks? Then what "
          "happened?* Their language was confused, and *\"they left off to build the city.\"*"),
    ask("And what were they trying to avoid in the first place? ...And what happened anyway?"),
    exp("Being scattered. They got scattered."),
    say("Isn't that something? They worked so hard to avoid the very thing God told them to do."),
    say("You can have a good plan, good friends, and everybody working together. But before you get too "
        "busy doing something, make sure you're going the direction God wants you to go."),

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
    say("Last week, Noah built because God told him to. This week, the people at Babel built to make a name "
        "for themselves. Both had plans. Both were builders. Both worked toward a goal. But only one was "
        "following God's instructions."),
    p(f"**{BIG}**"),
]

# ---- the inspector's sheet (a teacher plays her) ----
INSPECTOR = [
    "<h1>Building Inspector</h1>",
    f'<div class="sub">{TITLE} · Babel Construction Company</div>',
    p("**Who you are:** an overly serious government inspector. Your job is VERY important "
      "and you have no idea how ridiculous you are."),
    p("**Props:** clipboard, pen for extremely serious notes, tape measure, fake nose and glasses, "
      "2 REJECTED notices, APPROVED and REJECTED cards."),
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
    "<h2>About halfway: BOTH towers fail</h2>",
    p("Adjust your glasses. Concerned noises. *\"Mmmmm. No. No, no, no. Oh dear. This is not good.\"*"),
    p("**\"BOTH BUILDINGS HAVE FAILED INSPECTION!\"**"),
    p("Hand each team's CURRENT foreman a rejection notice. Only the foreman reads it. If they "
      "haven't fixed it when you come back: *\"Still rejected!\"*"),
    "<h2>Final inspection</h2>",
    p("Look at both towers: the other-color cups, how it looks, whatever concern you invent. "
      "When time's up, measure both towers first. Andrew asks who won, then asks who passed inspection: "
      "that's when you announce APPROVED or REJECTED for each, very seriously."),
    p("**When Andrew says you were rejecting everything in sight:** *\"And I'd do it again.\"*"),
    p("**If your favorite lost:** *\"EXCUSE ME?!\"* ... Andrew: *\"The rules said tallest tower wins.\"* "
      "... You: *\"Well, that's a terrible system.\"*"),
    p("**Optional, if it fits:** *\"These towers are impressive, but I have one question... "
      "WHO AUTHORIZED THIS CONSTRUCTION?\"*"),
]


# ---- station helper sheet (2 of the ladies, one per team) ----
HELPER = [
    "<h1>Station Helper</h1>",
    f'<div class="sub">{TITLE} · Babel Construction Company · one helper at the boys\' station, one at the girls\'</div>',
    p("**Your job:** keep your team's line moving and hand out the secret cards. Andrew runs the lesson; "
      "the inspector does the funny part. You keep the game running."),
    note("**The secret:** only HEIGHT wins. The inspector's rejections don't count. Don't tell them."),
    "<h2>Before the game</h2>",
    bullets("Your station: a firm board or table, your team's cup color, plus a few of the other color nearby.",
            "Get your foreman cards (one set of 10 per team).",
            "When Andrew starts the game, line your team up in groups of 3: a foreman and two builders."),
    "<h2>During the game</h2>",
    bullets("**Boys' station helper runs the buzzer:** every 30 seconds, call it out loud for BOTH teams.",
            "**First 30 seconds:** no cards, normal talking.",
            "**Every buzzer after that:** the 3 at the tower step out, the next 3 step in. Hand the new foreman "
            "a card, take the old card back. Only the foreman reads it.",
            "Builders don't read the cards or the rejection notice. Cover it if they peek.",
            "**When the inspector hands out the rejection notice:** make sure it passes foreman to foreman at "
            "each buzzer.",
            "Five rotations gets everyone one turn. Go around again if Andrew says keep going."),
    "<h2>When time is up</h2>",
    p("Everybody hands off, nobody touches the tower. The inspector measures. Andrew takes it from there."),
]

# ---- cards to print and cut ----
FOREMAN = ["Speak only in questions", "Sing every instruction", "Say your words in reverse order",
           "Only three words at a time", "Whisper every instruction", "Talk like a robot",
           "Narrate like a sports announcer", "Say everything dramatically",
           "Only say yes, no, or maybe", "Put a Bible verse in every instruction"]
CARD_CSS = """
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }
.card { border: 1.5px dashed #888; height: 1.8in; padding: 12pt; box-sizing: border-box;
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
    f'<div class="card"><div class="k">FOREMAN ONLY · DON\'T SHOW YOUR BUILDERS</div>'
    f'<div class="t">{esc(t)}</div><div class="s">Babel Construction Co.</div></div>'
    for t in FOREMAN)
REJ = ('<div class="rej"><div class="d">BABEL BUILDING DEPARTMENT</div><div class="big">INSPECTION FAILED</div>'
       '<div class="v">VIOLATION #11-4B</div><div class="body">This structure must contain a minimum of '
       "<b>FIVE cups of the opposing team's color</b>, located somewhere in <b>rows 3-5</b>.</div>"
       '<div class="body"><b>Correct immediately.</b><br>Construction may continue during repairs.</div>'
       '<div class="s">Foreman only. Pass this to the next foreman.</div></div>')
PRINT = (f"<style>{CARD_CSS}</style>"
         '<div class="sub">Cut on the dashed lines. 2 of each foreman card (one set per team).</div>'
         f'<div class="grid">{cards}</div><div class="pb"></div><div class="grid">{cards}</div>'
         f'<div class="pb"></div>{REJ}{REJ}'
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
FINAL = False
open(os.path.join(HERE, "index.html"), "w").write(web_page(
    os.path.basename(HERE), TITLE, "".join(body),
    ["Part - Inspector.pdf", "Part - Station helper.pdf", "Part - Cards to print.pdf"], final=FINAL))
mark = os.path.join(HERE, "FINAL")
if FINAL:
    open(mark, "w").close()
elif os.path.exists(mark):
    os.remove(mark)
print("done")
