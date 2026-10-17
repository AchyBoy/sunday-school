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
    p("1 student (or a teacher on the rotation). If they need a prompt: "
      "*a time you said sorry, and then actually changed.*"),

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

    h("4. God made a way", 3),
    p("Sin had to be judged, but God did not leave them there. He promised a Saviour "
      "from the woman's seed:"),
    scripture("Genesis 3:15"),
    p("And He covered them. Fig leaves were their idea. God's covering cost a life:"),
    scripture("Genesis 3:21"),
    p("Repentance is not a one time thing. Paul said:"),
    scripture("1 Corinthians 15:31"),
    p("Every day we put our flesh (our selfish nature) back on the altar. "
      "That is the *daily* in Luke 9:23."),

    h("5. Your story, or an illustration", 2),
    p("Pick one: a crew guy who kept saying sorry for the same mistake, a time YOU had to "
      "stop apologizing and fix it, or a time hiding made it worse. "
      "**Or** *The Pilgrim's Progress* (John Bunyan): Christian flees the City of Destruction "
      "and his burden rolls off at the cross."),

    h("6. What would you do?", 3),
    candy(3, "You lost your temper with your little brother Monday, Tuesday and Wednesday, "
             "and said sorry every time. It is Thursday morning. What do you do?",
          "EVERYONE who answers gets candy. Look for turning around: pray first, "
          "walk away, go to God before it happens again."),
    scripture("Acts 3:19"),
    p("**The big church:** the altar is where the church goes to repent. When you see people "
      "at the altar, now you know what is happening, and that it is for you too."),

    h("Prayer", 1),
    p("*Jesus, we admit that we are sinners today. We recognize that we have missed the mark of "
      "your righteousness time and time again. We're asking for You to forgive us. More "
      "importantly, we commit to repenting of our sin. From this day forward we will work to turn "
      "away from things that do not please You. Please give us the strength to live victoriously.*"),
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
