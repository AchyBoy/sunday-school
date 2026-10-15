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

N, S, E, A, G = NARRATOR, "Serpent", "Eve", "Adam", "The LORD God"
GARDEN = [
    ("#", "Scene 1: The serpent (Genesis 3:1-5)"),
    (N, "Now the serpent was more subtil than any beast of the field which the LORD God had made. And he said unto the woman,"),
    (S, "Yea, hath God said, Ye shall not eat of every tree of the garden?"),
    (N, "And the woman said unto the serpent,"),
    (E, "We may eat of the fruit of the trees of the garden: But of the fruit of the tree which is in the midst of the garden, God hath said, Ye shall not eat of it, neither shall ye touch it, lest ye die."),
    (N, "And the serpent said unto the woman,"),
    (S, "Ye shall not surely die: For God doth know that in the day ye eat thereof, then your eyes shall be opened, and ye shall be as gods, knowing good and evil."),
    ("#", "Scene 2: They eat (Genesis 3:6-7)"),
    (N, "And when the woman saw that the tree was good for food, and that it was pleasant to the eyes, and a tree to be desired to make one wise, she took of the fruit thereof, and did eat, and gave also unto her husband with her; and he did eat."),
    ("*", "Eve pretends to take a bite, then hands it to Adam. Adam bites."),
    (N, "And the eyes of them both were opened, and they knew that they were naked; and they sewed fig leaves together, and made themselves aprons."),
    ("#", "Scene 3: They hide (Genesis 3:8-13)"),
    (N, "And they heard the voice of the LORD God walking in the garden in the cool of the day: and Adam and his wife hid themselves from the presence of the LORD God amongst the trees of the garden."),
    ("*", "Adam and Eve hide behind a chair or table."),
    (N, "And the LORD God called unto Adam, and said unto him,"),
    (G, "Where art thou?"),
    (N, "And he said,"),
    (A, "I heard thy voice in the garden, and I was afraid, because I was naked; and I hid myself."),
    (N, "And he said,"),
    (G, "Who told thee that thou wast naked? Hast thou eaten of the tree, whereof I commanded thee that thou shouldest not eat?"),
    (N, "And the man said,"),
    (A, "The woman whom thou gavest to be with me, she gave me of the tree, and I did eat."),
    ("*", "Adam points at Eve."),
    (N, "And the LORD God said unto the woman,"),
    (G, "What is this that thou hast done?"),
    (N, "And the woman said,"),
    (E, "The serpent beguiled me, and I did eat."),
    ("*", "Eve points at the Serpent."),
    ("#", "Scene 4: Judgment and hope (Genesis 3:14-19)"),
    (N, "And the LORD God said unto the serpent,"),
    (G, "Because thou hast done this, thou art cursed above all cattle, and above every beast of the field; upon thy belly shalt thou go, and dust shalt thou eat all the days of thy life: And I will put enmity between thee and the woman, and between thy seed and her seed; it shall bruise thy head, and thou shalt bruise his heel."),
    ("*", "Serpent drops to the floor."),
    (N, "Unto the woman he said,"),
    (G, "I will greatly multiply thy sorrow and thy conception; in sorrow thou shalt bring forth children; and thy desire shall be to thy husband, and he shall rule over thee."),
    (N, "And unto Adam he said,"),
    (G, "Because thou hast hearkened unto the voice of thy wife, and hast eaten of the tree, of which I commanded thee, saying, Thou shalt not eat of it: cursed is the ground for thy sake; in sorrow shalt thou eat of it all the days of thy life; Thorns also and thistles shall it bring forth to thee; and thou shalt eat the herb of the field; In the sweat of thy face shalt thou eat bread, till thou return unto the ground; for out of it wast thou taken: for dust thou art, and unto dust shalt thou return."),
    ("#", "Scene 5: Out of the garden (Genesis 3:20-24)"),
    (N, "And Adam called his wife's name Eve; because she was the mother of all living. Unto Adam also and to his wife did the LORD God make coats of skins, and clothed them."),
    (N, "And the LORD God said, Behold, the man is become as one of us, to know good and evil: and now, lest he put forth his hand, and take also of the tree of life, and eat, and live for ever: Therefore the LORD God sent him forth from the garden of Eden, to till the ground from whence he was taken."),
    (N, "So he drove out the man; and he placed at the east of the garden of Eden Cherubims, and a flaming sword which turned every way, to keep the way of the tree of life."),
    ("*", "Adam and Eve walk out. The Cherubims step in front of the \"tree\" and cross the sword."),
]
GARDEN_CAST = [(N, "(you)"), (S, ""), (E, ""), (A, ""), (G, "(a teacher)"),
               ("Cherubims", "(2 kids, no lines, hold the pool noodle sword)")]

body = [
    f"<h1>{TITLE}</h1>",
    '<div class="sub">Genesis 3 · Series 1: In the Beginning · '
    "Big idea: <b>Sorry is not enough. Repentance is turning around.</b></div>",
    scripture("Luke 9:23", "Key verse: Luke 9:23"),
    note("**Bring:** candy · Skittles + a cup · pool noodle (flaming sword) · "
         "a \"fruit\" (an apple or a ball) · a few birthday candles or party hats · part sheets printed"),

    h("1. Testimony", 5),
    p("1 or 2 students (or a teacher on the rotation). If they need a prompt: "
      "*a time you said sorry, and then actually changed.*"),

    h("2. Act it out: The Birthday Candles", 5),
    script("The Birthday Candles", CANDLES_CAST, CANDLES),
    candy(1, "He said sorry three times. Was he lying? Then what was missing?",
          "Maybe he really was sorry. But he never CHANGED. Sorry is a feeling. "
          "Repentance is turning around."),

    h("3. The perfect garden", 5),
    p("God made everything good, and He made man for one reason: to walk with Him. "
      "In the middle of the garden He planted two trees."),
    scripture("Genesis 2:9"),
    scripture("Genesis 2:16-17"),
    bullets("The tree of life: God wanted them to live for ever.",
            "The other tree: God put it there so they had a CHOICE. "
            "Love you are forced into is not love."),

    '<div class="pb"></div>',
    h("4. Act it out: Genesis 3", 15),
    p("You read the Narrator. The kids read their parts off their sheets. "
      "This IS the scripture reading, so there is nothing to look up."),
    script("The Garden (Genesis 3, KJV)", GARDEN_CAST, GARDEN),
    candy(2, "Count them. How many times did Adam or Eve say \"I'm sorry\"? "
             "And who did Adam blame?",
          "ZERO. Adam blamed the woman, AND God: \"the woman whom THOU gavest.\" "
          "Eve blamed the serpent. Follow up, no candy: *who do YOU blame?*"),

    h("5. The altar", 10),
    p("Notice verse 21: God made them coats of skins. Something had to die to cover them. "
      "In the Old Testament, the sacrifice was tied to the altar so it could not crawl off."),
    scripture("Psalms 118:27"),
    p("Our flesh (not our body, our selfish nature) is that sacrifice. It wants to crawl off "
      "the altar every day. So we put it back every day."),
    scripture("1 Corinthians 15:31"),
    scripture("Galatians 5:24"),
    p("Back to Luke 9:23: take up his cross **daily**. Repentance is not a one time thing."),
    p("**The big church:** the altar is where the church goes to repent. When you see people "
      "at the altar on Sunday night, now you know what is happening, and that it is for you too."),

    h("6. Object lesson: the cup", 5),
    bullets("The cup is us. The candy is the things of God: blessings, purpose, understanding.",
            "Turn the cup upside down. Ask: *\"If I pour these on it, will any get in?\"* Pour.",
            "Turn it right side up. Same question. Pour.",
            "Repentance turns us right side up so we can receive from God."),

    h("7. Your story, or an illustration", 5),
    p("Pick one of these prompts:"),
    bullets("A crew guy who kept making the same mistake and kept saying sorry. What finally changed?",
            "A time YOU had to stop apologizing and just fix it.",
            "A time hiding something made it worse than owning it."),
    p("**Or a book:** *The Pilgrim's Progress*, by John Bunyan. Christian lives in the "
      "City of Destruction with a heavy burden on his back. He runs for the Celestial City, "
      "and at the cross his burden rolls off. Tell it in your own words."),

    h("8. What would you do?", 5),
    candy(3, "You lost your temper with your little brother Monday, Tuesday and Wednesday, "
             "and said sorry every time. It is Thursday morning. What do you do?",
          "EVERYONE who answers gets candy. Look for turning around: pray first, "
          "walk away, go to God before it happens again."),
    scripture("Acts 3:19"),
    scripture("1 John 1:9"),

    h("Prayer"),
    p("*Jesus, we admit that we are sinners today. We recognize that we have missed the mark of "
      "your righteousness time and time again. We're asking for You to forgive us. More "
      "importantly, we commit to repenting of our sin. From this day forward we will work to turn "
      "away from things that do not please You. Please give us the strength to live victoriously.*"),
]

out = os.path.join(HERE, "pdf")
os.makedirs(out, exist_ok=True)
to_pdf(page(TITLE, "".join(body)), os.path.join(out, "1.2 Teacher - Dealing With Our Sin.pdf"))

HOW = {
    "Birthday Kid": "It's your birthday. You keep forgiving your friend, until the third time.",
    "Best Friend": "You blow out the candles three times. Each time, mean it when you say sorry.",
    "Parent": "You light the candles and count everyone in to sing.",
    "Guests": "Everyone else. Sing Happy Birthday each time the Parent counts you in.",
    "Serpent": "You are sneaky. You never tell a flat lie, you twist what God said.",
    "Eve": "You talk to the serpent, eat the fruit, and give some to Adam.",
    "Adam": "You eat the fruit, hide, and then blame Eve. Point at her on your last line.",
    "The LORD God": "Read slowly and with authority. You already know what they did.",
}
for role in ["Birthday Kid", "Best Friend", "Parent", "Guests"]:
    to_pdf(part_sheet(TITLE, "The Birthday Candles", role, HOW[role], CANDLES),
           os.path.join(out, f"Part - {role}.pdf"))
for role in [S, E, A, G]:
    to_pdf(part_sheet(TITLE, "The Garden (Genesis 3)", role, HOW[role], GARDEN),
           os.path.join(out, f"Part - {role}.pdf"))
print("done")
