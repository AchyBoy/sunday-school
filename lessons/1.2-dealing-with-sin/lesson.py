import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from lib import *

TITLE = "Lesson 1.2: Dealing With Our Sin"

CANDLES = [
    ("#", "The party"),
    ("*", "Birthday Kid stands at the table. Guests gather around. Parent \"lights\" the candles."),
    ("Parent", "Okay everybody, here comes the cake! Ready? One, two, three..."),
    ("Guests", "Happy birthday to you..."),
    ("*", "Best Friend cuts in front and blows out the candles."),
    ("Birthday Kid", "Hey! What did you do that for?"),
    ("Best Friend", "Oh, I am so sorry. I shouldn't have done that."),
    ("Birthday Kid", "It's okay. I forgive you."),
    ("Parent", "Let's try again. One, two, three..."),
    ("Guests", "Happy birthday to you, happy birthday to you..."),
    ("*", "Best Friend cuts in again and blows out the candles."),
    ("Birthday Kid", "Why did you do that?"),
    ("Best Friend", "I don't know. I just couldn't help myself. I'm sorry."),
    ("Birthday Kid", "Fine. I forgive you. But don't do it again."),
    ("Parent", "Last time. One, two, three..."),
    ("Guests", "Happy birthday to you, happy birthday dear friend, happy birthday..."),
    ("*", "Best Friend bursts in and blows out ALL the candles."),
    ("Birthday Kid", "STOP IT!"),
    ("Best Friend", "I'm so sorry..."),
    ("Parent", "Forget it. I'm just cutting the cake. Worst birthday ever."),
]
CANDLES_CAST = [("Birthday Kid", ""), ("Best Friend", ""), ("Parent", ""),
                ("Guests", "(everyone else sings)")]

body = [
    f"<h1>{TITLE}</h1>",
    '<div class="sub">Genesis 3 · Series 1: In the Beginning · About 20 minutes · '
    "Big idea: <b>Sorry is not enough. Repentance is turning around.</b></div>",
    scripture("Luke 9:23", "Key verse: Luke 9:23"),
    note("**Bring:** candy · a cake or a paper plate \"cake\" with a few candles · "
         "the 4 candle part sheets printed"),

    h("1. Testimony", 2),
    p("One student, or one of us teachers, gives a testimony. If they get stuck, I'll ask: "
      "*tell us about a time you said sorry, and then actually changed.*"),

    h("2. Act it out: The Birthday Candles", 4),
    script("The Birthday Candles", CANDLES_CAST, CANDLES),
    candy(1, "How many times did he say he was sorry? Then why did he keep doing it?",
          "Three times. He never CHANGED. Sorry is a feeling. "
          "Repentance is turning around."),

    h("3. What happened in the garden", 6),
    p("God made everything good, and He made man to walk with Him. He gave Adam one rule."),
    scripture("Genesis 2:17"),
    p("The serpent got her to doubt God first: *\"Yea, hath God said...?\"* "
      "Then he called God a liar: *\"Ye shall not surely die.\"*"),
    scripture("Genesis 3:4-6"),
    p("Now watch what they do when God comes walking."),
    scripture("Genesis 3:8-13"),
    candy(2, "Count them. How many times did Adam or Eve say \"I'm sorry\"? "
             "And who did Adam blame?",
          "ZERO. Adam blamed the woman, AND God: \"the woman whom THOU gavest.\" "
          "Eve blamed the serpent. Follow up, no candy: *who do YOU blame?*"),
    p("God gave the rule to Adam. Adam was the leader, and he was right there: "
      "*\"her husband with her.\"* If he had made up the hedge and stood in the gap, God "
      "wouldn't have had to step in. That's what God wants:"),
    scripture("Ezekiel 22:30"),

    h("4. God made a way", 4),
    p("Sin had to be judged, but God did not leave them there. He promised a Saviour "
      "from the woman's seed:"),
    scripture("Genesis 3:15"),
    p("And He covered them. Fig leaves were their idea. God's covering cost a life:"),
    scripture("Genesis 3:21"),
    p("That animal covered them for a while, but it pointed to Jesus:"),
    scripture("Hebrews 10:4"),
    funfact("Jesus walked it back",
        "When Adam sinned, three things came in, in this order:",
        ["**1. The tree:** *\"she took of the fruit thereof, and did eat, and gave also unto her husband "
        "with her; and he did eat.\"* (Genesis 3:6)",
        "**2. The thorns:** *\"Thorns also and thistles shall it bring forth to thee.\"* (Genesis 3:18)",
        "**3. The sweat:** *\"In the sweat of thy face shalt thou eat bread.\"* (Genesis 3:19)"],
        "Jesus met all three, backwards:",
        ["**1. The sweat:** *\"his sweat was as it were great drops of blood.\"* (Luke 22:44)",
        "**2. The thorns:** *\"they had platted a crown of thorns, they put it upon his head.\"* (Matthew 27:29)",
        "**3. The tree:** *\"Who his own self bare our sins in his own body on the tree.\"* (1 Peter 2:24)"],
        "Adam failed in a garden. Jesus won in a garden, and ended up right back at a tree. "
        "The thorns were the curse, and they put the curse on His head."),
    p("Repentance is not a one time thing. Back to our key verse, Jesus said *daily*:"),
    scripture("Luke 9:23"),
    p("Every day we put our flesh (our selfish nature) back on the altar."),

    h("5. My story", 2),
    p("**My story, as a teenager:** I didn't want to repent. I was having a good time with my "
      "sneaky stuff, but I knew what it was going to cost. I didn't want to, and at the same time "
      "I wanted to, because I knew I needed to."),

    h("6. What would you do?", 3),
    candy(3, "You lost your temper with your little brother Monday, Tuesday and Wednesday, "
             "and said sorry every time. It is Thursday morning. What do you do?",
          "EVERYONE who answers gets candy. Good answers: turning around, pray first, "
          "walk away, go to God before it happens again."),
    scripture("Acts 3:19"),
    p("**The big church:** the altar isn't only for when you've done something bad. It's where "
      "you go to turn around, any time. So when you see grown ups at the altar, it doesn't mean "
      "they're bad. They're doing what we just learned."),

    h("Prayer", 1),
    p("• Lord, help me first see where I'm wrong."),
    p("• Help me be honest with myself: have I really repented?"),
    p("• Do I even want to? If I don't, help me with that too."),
]

out = os.path.join(HERE, "pdf")
os.makedirs(out, exist_ok=True)

HOW = {
    "Birthday Kid": "It's your birthday. You keep forgiving your friend, until the third time.",
    "Best Friend": "You blow out the candles three times. Each time, mean it when you say sorry.",
    "Parent": "You light the candles and count everyone in to sing.",
    "Guests": "Everyone else. Sing Happy Birthday each time the Parent counts you in.",
}
for f in os.listdir(out):
    os.remove(os.path.join(out, f))
to_pdf(page(TITLE, "".join(body)), os.path.join(out, "1.2 Teacher - Dealing With Our Sin.pdf"))
for role in HOW:
    to_pdf(part_sheet(TITLE, "The Birthday Candles", role, HOW[role], CANDLES),
           os.path.join(out, f"Part - {role}.pdf"))
# FINAL = he has signed off; until then the site shows the marked-up web copy first.
FINAL = False
open(os.path.join(HERE, "index.html"), "w").write(web_page(
    os.path.basename(HERE), TITLE, "".join(body),
    [f"Part - {r}.pdf" for r in HOW], final=FINAL))
mark = os.path.join(HERE, "FINAL")  # build_index.py reads this
if FINAL:
    open(mark, "w").close()
elif os.path.exists(mark):
    os.remove(mark)
print("done")
