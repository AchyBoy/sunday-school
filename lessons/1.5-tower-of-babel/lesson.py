import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from lib import *

# Built from his FINAL PLANNING NOTES (2026-11-18). Teacher copy in his voice, conversational.
TITLE = "Lesson 1.5: The Tower of Babel"
BIG = "Just because you're busy building something doesn't mean you're building what God told you to build."

body = [
    f"<h1>{TITLE}</h1>",
    '<div class="sub">Genesis 11:1-9 · Series 1: In the Beginning · Ages 14-17, about 30 kids · '
    f"About 25-30 minutes · Big idea: <b>{esc(BIG)}</b></div>",
    '<div class="sub">Written by Andrew Young</div>',
    note("**Bring:** 2 firm boards or tables (carpet) · 2 colors of plastic cups · 30-second timer · "
         "the printed cards (foreman cards, 2 rejection notices, APPROVED / REJECTED) · inspector's "
         "clipboard, pen, tape measure, fake nose and glasses · candy. "
         "**Before class:** test the cups on the boards, brief the inspector, agree when she does the "
         "rejection. **During the opening:** a few boys quietly set up the two stations."),

    h("1. Opening: Noah", 5),
    p("Who remembers what we talked about last week?"),
    p("What did Noah build? ...Right, the ark."),
    p("So did Noah just wake up one morning and go, \"You know what? I want a giant boat\"?"),
    p("No. God told him to build it. And when they came off the ark, God gave them a job:"),
    scripture("Genesis 9:1"),
    p("Replenish the earth. Spread out and fill it up."),
    p("Now, a few generations later, we've got another group of people who decide to build something "
      "massive. But there's one pretty big difference. Noah built because God told him to. "
      "These people wanted to make a name for themselves."),
    scripture("Genesis 11:1-4"),
    p("Did y'all catch that? *\"Let us make us a name.\"* And *\"lest we be scattered abroad.\"*"),
    candy(1, "What did God tell Noah's family to do? And what are these people trying to avoid doing?",
          "Fill the earth (Genesis 9:1). They're trying NOT to be scattered. Let them make the "
          "connection themselves."),
    funfact("They really did stamp a name on the bricks",
        "In the Bible, Babel and Babylon are the same word. Centuries later, King Nebuchadnezzar "
        "(the one from Daniel) rebuilt Babylon and stamped HIS NAME into the bricks. Archaeologists "
        "have dug up thousands of them, and museums have them today. Same city, same idea: "
        "*\"let us make us a name.\"*",
        "*For me:* the bricks are from long after the tower, so this is a connection, not something "
        "Genesis says. Nebuchadnezzar said it himself in Daniel 4:30: *\"Is not this great Babylon, "
        "that I have built... for the honour of my majesty?\"*"),
    p("**Life lesson:** having a good plan doesn't automatically mean it's God's plan."),

    h("2. Before the game: they were united", 6),
    scripture("Genesis 11:5-6"),
    funfact("They built up, God came down",
        "They built a tower *\"whose top may reach unto heaven.\"* And verse 5 says *\"the LORD came "
        "down to see\"* it. Their biggest thing ever, and God still had to come down to look at it.",
        "*If they want more:* look at their words, *\"Go to, let us...\"* (verses 3 and 4). God answers "
        "with their own words in verse 7: *\"Go to, let us go down.\"*"),
    p("Look what God Himself says about them: *\"the people is one, and they have all one language.\"* "
      "Everybody was working together. Everybody had the same goal. And it worked, they were good at it. "
      "But what they were working toward was the opposite of what God said to do."),
    p("Have y'all ever been with a group of friends where everybody agreed to do something stupid?"),
    p("**Life lesson:** just because everybody agrees doesn't mean everybody is right."),
    p("They had one language, so they could coordinate everything. Bricks, slime, who's carrying what."),
    note("**Don't read verses 7-9 yet.**"),
    p("So these people had the materials, the manpower, and a plan. But how much of their success "
      "depended on being able to understand each other?"),
    p("Well... we're about to find out."),

    h("3. Babel Construction Company", 10),
    bullets("Boys vs. girls, one station each, about 15 per team.",
            "One **foreman** and two **builders** per team at a time. Everyone else waits in line.",
            "Every **30 seconds** the buzzer goes and all three rotate out. Five rotations = everyone "
            "gets a turn. Run more if there's time.",
            "**First 30 seconds:** normal talking. After the first buzzer, every new foreman gets a "
            "secret card. Only the foreman reads it.",
            "The inspector roams the whole time. She never stops the game."),
    p("**The announcement (I read it out loud):**"),
    p("Welcome to Babel Construction Company! Each team will be constructing the tallest tower possible "
      "using the materials provided."),
    p("**THE WINNER WILL BE DETERMINED BY THE FINAL HEIGHT OF THEIR STANDING TOWER.**"),
    p("Now, a few things you need to know. You'll have a foreman and two builders working at a time. "
      "Every 30 seconds, the buzzer will sound, and all three will be replaced. Each new foreman will "
      "receive a special communication instruction that must be followed at all times."),
    p("Our official building inspector will be conducting inspections throughout construction. She has "
      "the authority to issue rejection notices, require modifications, and demand immediate corrections "
      "to building-code violations. All rejection notices must be communicated by the foreman to the "
      "builders. Builders may not read rejection notices. At the conclusion, the inspector will conduct a "
      "final inspection and issue an official approval or rejection."),
    p("Any questions? ...Good. Because I probably wasn't going to answer them anyway."),
    p("**LET THE CONSTRUCTION BEGIN!**"),
    note("**Only height wins.** The inspector's approvals, rejections and building codes do NOT count. "
         "Don't remind them until the end."),
    p("**About halfway:** the inspector fails BOTH towers and hands each foreman a rejection notice: "
      "five cups of the other team's color somewhere in rows 3-5. The foreman has to explain it under "
      "their card's rule, and passes the notice to the next foreman. The timer never stops."),
    p("**When time is up:** everybody stops. The inspector does her final inspection, APPROVED or "
      "REJECTED (just for show). Then I ask:"),
    p("Okay. Which team actually won?"),
    p("She measures. Tallest standing tower wins. (If the inspector's favorite LOST, she gets to be "
      "outraged: *\"EXCUSE ME?!\"* · *\"The rules said tallest tower wins.\"* · "
      "*\"Well, that's a terrible system.\"*)"),

    h("4. Who authorized this?", 2),
    p("Did I tell y'all how to win? ...What did I say? ...Build the tallest tower."),
    p("Then why were y'all so worried about making the inspector happy?"),
    p("You got so busy following all these other instructions that you lost sight of the original one."),
    p("**Inspector:** *\"These towers are impressive, but I have one question... "
      "WHO AUTHORIZED THIS CONSTRUCTION?\"*"),
    p("That's actually a very good question. Because when we left off in Genesis 11, the people were "
      "building something impressive. But who told them to build it?"),

    h("5. Finish the story", 6),
    scripture("Genesis 11:7-9"),
    candy(2, "Did God knock their tower down?",
          "No! The Bible never says the tower fell. They didn't run out of bricks, and they didn't forget "
          "how to build. What changed? Their language. And *\"they left off to build the city.\"*"),
    p("They built that tower so they wouldn't be scattered. And what happened? They got scattered."),
    bullets("**Genesis 9:1**, God's command: fill the earth.",
            "**Genesis 11:4**, man's plan: stay together and make a name for ourselves.",
            "**Genesis 11:8**, God's answer: they were scattered."),
    p("**Life lesson:** you can be busy, talented, successful, and surrounded by people who agree with "
      "you, and still be heading in the wrong direction."),
    p("Have you ever been so focused on doing something that you forgot why you were doing it?"),
    p("Do you ever stop and ask God whether what you're working toward is actually what He wants?"),
    scripture("Proverbs 3:5-6"),
    note("**For me:** Genesis doesn't say they forgot God's command or that they didn't pray. Those are "
         "questions for US, not facts about them."),

    h("6. If there's time: Pentecost", 3),
    p("At Babel, they all had one language, and they used it to make their own name great. "
      "At Pentecost, people from every nation heard, each in his own language..."),
    scripture("Acts 2:4-11"),
    p("...*\"the wonderful works of God.\"* The difference isn't one language or many languages. "
      "It's whose name is being lifted up. (And look at verse 6: the crowd was *\"confounded,\"* the same "
      "word as Babel. Only this time God was the one getting the attention.)"),

    h("7. Closing", 3),
    p("Last week, we learned about Noah. Noah built because God told him to."),
    p("This week, we learned about people who built because they wanted to make a name for themselves."),
    p("Both had plans. Both were builders. Both were working toward something. "
      "But only one was following God's instructions."),
    p("There's nothing wrong with having ambition, working hard, or wanting to accomplish something. "
      "But we need to make sure that what we're building is what God wants us to build."),
    candy(3, "What would you do? Your friends all agree on a plan for the weekend. It's fun, nobody "
             "thinks it's bad, but nobody has asked God either. What do you do?",
          "EVERYONE who answers gets candy."),
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
      "Give each one APPROVED or REJECTED. Then Andrew asks which team actually won, and you measure."),
    p("**If your favorite lost:** *\"EXCUSE ME?!\"* ... Andrew: *\"The rules said tallest tower wins.\"* "
      "... You: *\"Well, that's a terrible system.\"*"),
    p("**Your last line, after Andrew asks why they worried about you:** "
      "*\"These towers are impressive, but I have one question... WHO AUTHORIZED THIS CONSTRUCTION?\"*"),
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
to_pdf(page("Cards to print", PRINT), os.path.join(out, "Part - Cards to print.pdf"))
FINAL = False
open(os.path.join(HERE, "index.html"), "w").write(web_page(
    os.path.basename(HERE), TITLE, "".join(body),
    ["Part - Inspector.pdf", "Part - Cards to print.pdf"], final=FINAL))
mark = os.path.join(HERE, "FINAL")
if FINAL:
    open(mark, "w").close()
elif os.path.exists(mark):
    os.remove(mark)
print("done")
