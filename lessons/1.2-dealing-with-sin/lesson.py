import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from lib import *

TITLE = "Lesson 1.2: Dealing With Our Sin"

SORRY = [
    ("Jake", "Bro, why did you tell everybody I screamed when that little dog chased me?"),
    ("Tyler", "Because you did scream."),
    ("Jake", "It was not a scream!"),
    ("Marcus", "I heard it from inside the house."),
    ("Ben", "I thought somebody was getting kidnapped."),
    ("Jake", "It was a very aggressive dog!"),
    ("Tyler", "It was a Chihuahua."),
    ("Jake", "THAT DOESN'T MATTER!"),
    ("Tyler", "Okay, okay. I'm sorry. I shouldn't have told everybody."),
    ("Jake", "Thank you. Just stop telling people."),
    ("Tyler", "I got you, bro."),
    ("Ben", "So what are y'all doing after church?"),
    ("Tyler", "I don't know. Probably going to Jake's house. Hopefully his mom doesn't make him eat vegetables again."),
    ("Jake", "Tyler!"),
    ("Marcus", "Wait, what?"),
    ("Tyler", "Oh, last week his mom made broccoli, and Jake sat there gagging like he was dying."),
    ("Ben", "Over broccoli?!"),
    ("Jake", "I TOLD YOU THAT IN PRIVATE!"),
    ("Tyler", "My bad, bro. I'm sorry."),
    ("Jake", "You just apologized for doing the exact same thing!"),
    ("Tyler", "And I meant it!"),
    ("Jake", "Then STOP DOING IT!"),
    ("Tyler", "Okay! I won't do it again. Promise."),
    ("Marcus", "So, Jake, you coming to play basketball Saturday?"),
    ("Jake", "Yeah, probably."),
    ("Tyler", "As long as he doesn't shoot any three-pointers."),
    ("Jake", "Tyler. Don't."),
    ("Ben", "Why not?"),
    ("Tyler", "Because last time he shot one, it went over the backboard and hit somebody's grandma."),
    ("Marcus", "NO WAY!"),
    ("Jake", "IT DID NOT HIT HER! IT LANDED NEXT TO HER!"),
    ("Tyler", "See? He's still sensitive about it."),
    ("Jake", "BRO! YOU HAVE GOT TO BE KIDDING ME!"),
    ("Tyler", "What?! I'm sorry!"),
    ("Jake", "BRO! YOU KEEP SAYING YOU'RE SORRY!"),
    ("Tyler", "Well, I AM sorry!"),
    ("Jake", "THEN WHY DO YOU KEEP DOING IT?!"),
    ("Ben", "I'm starting to think he doesn't know what sorry means."),
    ("Marcus", "He knows how to say it. That's about it."),
    ("Tyler", "Man, y'all are making a big deal out of nothing."),
    ("Jake", "And THAT is why I don't believe you're sorry!"),
]
SORRY_CAST = [("Jake", ""), ("Tyler", ""), ("Marcus", ""), ("Ben", "")]

body = [
    f"<h1>{TITLE}</h1>",
    '<div class="sub">Genesis 3 · Series 1: In the Beginning · About 20 minutes · '
    "Big idea: <b>Sorry is not enough. Repentance is turning around.</b></div>",
    scripture("Luke 9:23", "Key verse: Luke 9:23"),
    note("**Bring:** candy · the 4 part sheets printed"),

    h("1. Testimony", 2),
    p("One student, or one of us teachers, gives a testimony. If they get stuck, I'll ask: "
      "*tell us about a time you said sorry, and then actually changed.*"),

    h("2. Act it out: Bro, I Said Sorry!", 4),
    p("Four boys: Jake, Tyler, Marcus, Ben. Hand out the parts and read straight through. "
      "No props, no moving around, no practice needed."),
    script("Bro, I Said Sorry!", SORRY_CAST, SORRY),
    candy(1, "How many times did Tyler say he was sorry? Then why did he keep doing it?",
          "Three times. He kept doing the same thing, and then defended it. Repentance means "
          "really turning away from sin, not becoming perfect overnight. When we fail, we admit "
          "it and turn back toward God."),
    p("We can say sorry to God and keep right on doing it. Saying it is confessing. "
      "Turning away is forsaking. God wants both:"),
    scripture("Proverbs 28:13"),

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
    p("God told Adam not to eat the fruit. But when Eve repeated the command, she said they "
      "weren't even supposed to *touch* it! God gave that command to Adam before Eve was "
      "created, so it makes sense Adam taught her. Maybe he added that extra rule about "
      "touching it. The Bible doesn't tell us who added it."),
    p("But Adam knew what God said. Eve ate, and Adam was right there with her. He could have "
      "stood for God's command. Instead, he ate too! How can you tell somebody else to obey God "
      "when you won't obey Him yourself?"),
    p("One day some of you will be husbands, fathers, and leaders. You can't lead somebody "
      "somewhere you're not willing to go yourself. God calls men to stand for what's right, "
      "not just know His Word, but live it. A godly leader doesn't have to be perfect. He needs "
      "to admit when he's wrong, repent, and lead by example."),
    scripture("Ezekiel 22:30"),
    p("That verse describes a different situation, but the principle fits: stand for what is "
      "right. Adam didn't stand. He joined in, then blamed everybody but himself."),

    h("4. God made a way", 4),
    p("Sin had to be judged, but God did not leave them there. He promised a Saviour "
      "from the woman's seed:"),
    scripture("Genesis 3:15"),
    p("And He covered them. Fig leaves were their idea, but God made coats of skins for them. "
      "That covering cost a life. They couldn't fix what they'd done themselves, so God had to "
      "provide what they couldn't. And that points us to Jesus. No animal sacrifice could ever "
      "take away sin. Only Jesus could do that."),
    scripture("Genesis 3:21"),
    scripture("Hebrews 10:4"),
    funfact("Jesus walked it back",
        "When Adam sinned, three things came in: the tree, the thorns, and the sweat. "
        "Jesus met all three, backwards.",
        "**1. The sweat:** Adam sweat because he did it his way. Jesus sweat to do it God's way, "
        "so we can rest instead of sweating for it.",
        "*For me, if they ask:* Adam: *\"In the sweat of thy face shalt thou eat bread, till thou "
        "return unto the ground\"* (Genesis 3:19). Jesus in the garden: *\"nevertheless not my will, "
        "but thine, be done... and his sweat was as it were great drops of blood falling down to the "
        "ground\"* (Luke 22:42, 44). Adam lost in a garden doing his own will. Jesus won in a garden "
        "by giving His up. For us: *\"Come unto me, all ye that labour and are heavy laden, and I will "
        "give you rest\"* (Matthew 11:28). We still work, but we don't sweat to earn our way back to God.",
        "**2. The thorns:** Adam traded his crown for thorns. Jesus wore the thorns to win the crown back.",
        "*For me, if they ask:* Adam was made king over the earth: *\"have dominion over the fish of the "
        "sea, and over the fowl of the air, and over every living thing\"* (Genesis 1:28). After he sinned "
        "the ground turned on him: *\"Thorns also and thistles shall it bring forth to thee\"* (Genesis 3:18). "
        "They mocked Jesus as a king with that curse: *\"they had platted a crown of thorns, they put it "
        "upon his head... Hail, King of the Jews!\"* (Matthew 27:29). He was *\"made a curse for us\"* "
        "(Galatians 3:13). Hebrews 2 ties it to Adam's crown itself: *\"But now we see not yet all things "
        "put under him. But we see Jesus... for the suffering of death, crowned with glory and honour\"* "
        "(Hebrews 2:8-9).",
        "**3. The tree:** Adam took from a tree to make himself God. God gave Himself on a tree to bring "
        "us back. Adam was naked, then God clothed him. Jesus was clothed, then they stripped Him naked.",
        "*For me, if they ask:* The serpent: *\"ye shall be as gods\"* (Genesis 3:5). Jesus: *\"thought it "
        "not robbery to be equal with God: But made himself of no reputation... and became obedient unto "
        "death, even the death of the cross\"* (Philippians 2:6, 8). Adam was *\"naked... and were not "
        "ashamed\"* (Genesis 2:25), sinned, hid in shame, and God *\"made coats of skins, and clothed "
        "them\"* (Genesis 3:21). Jesus went the other way. The soldiers *\"took his garments, and made four "
        "parts... and also his coat\"* and gambled for it (John 19:23-24). The Bible doesn't say the word "
        "naked, but they took all of it, and the Romans usually crucified people naked to shame them. The "
        "cloth in paintings is church art. He *\"endured the cross, despising the shame\"* (Hebrews 12:2), "
        "so we could be clothed: *\"he hath clothed me with the garments of salvation, he hath covered me "
        "with the robe of righteousness\"* (Isaiah 61:10). Adam was shut out from the tree of life "
        "(Genesis 3:24). Through Jesus: *\"that they may have right to the tree of life\"* (Revelation 22:14).",
        "*If they ask why we still sweat and thorns still grow:* He fixed it spiritually now. The ground "
        "and our bodies are still waiting: *\"And there shall be no more curse\"* (Revelation 22:3)."),
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
    "Jake": "Your friend Tyler keeps telling everybody your embarrassing stuff. You get louder every time.",
    "Tyler": "You keep telling Jake's secrets, and you keep saying sorry. Say it like you mean it every time.",
    "Marcus": "You're one of the friends. You can't believe what you're hearing.",
    "Ben": "You're one of the friends. You ask the questions that get Tyler going.",
}
for f in os.listdir(out):
    os.remove(os.path.join(out, f))
to_pdf(page(TITLE, "".join(body)), os.path.join(out, "1.2 Teacher - Dealing With Our Sin.pdf"))
for role in HOW:
    to_pdf(part_sheet(TITLE, "Bro, I Said Sorry!", role, HOW[role], SORRY),
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
