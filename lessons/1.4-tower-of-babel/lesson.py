import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from lib import *

# ROUND 1 = an IDEA MENU, every idea numbered so he can say "I like 3, tweak 7".
# He doesn't have the book with him, so everything sits on Genesis 11:1-9 itself.
TITLE = "Lesson 1.4: The Tower of Babel"

body = [
    f"<h1>{TITLE}</h1>",
    '<div class="sub">Genesis 11:1-9 · Ages 14-17, about 30 kids · '
    "Lesson about 15 min + activity about 10 min</div>",
    note("**Idea menu, round 1.** Every idea has a number. Tap ✎ on any of them: keep it, "
         "cut it, or tell me what to change. I'll build the final lesson from what you pick."),

    h("The passage"),
    scripture("Genesis 11:1-9"),

    "<h2>Pick ONE activity (about 10 min)</h2>",
    h("1. Silent tower build"),
    p("Teams of 6 race to build the tallest tower out of cups or index cards and tape, 3 minutes. "
      "At 90 seconds every kid gets a secret card: *only talk in questions · only Spanish · "
      "no talking, only humming · every sentence starts with \"Banana\" · disagree with the last "
      "person who spoke.* The towers fall apart. The lesson shows itself."),
    p("**Needs:** about 150 cups or 5 packs of index cards + tape, 30 printed cards."),
    h("1b. Boys build a human pyramid, girls stack cups (your idea)"),
    p("**2-minute clock. Whoever is HIGHEST when the timer goes off wins.** Not the highest you ever "
      "got, the highest at the buzzer. Build early and you have to hold it the rest of the time. "
      "Wait too long and you might not finish. The team decides when to go up."),
    p("**Boys:** teams of 6 build a kneeling pyramid, 3 on the bottom, 2, then 1. If two teams are "
      "both up at the buzzer, the tape measure decides (floor to the top kid's back). "
      "**Girls:** teams build the tallest cup tower they can, any shape. Same rule: it only counts "
      "if it's still standing at the buzzer. Hand out the secret language cards at the start, so "
      "every team has to plan its timing while nobody understands each other."),
    p("**Safety rules for the pyramid:** hands and knees only, nobody stands up, no more than 3 rows, "
      "on carpet or mats, shoes off, and 2 spotters at each pyramid. If the bottom row says down, "
      "everybody comes down. **Ask the pastor first:** some churches have rules about stunts like this."),
    p("**Needs:** about 150 plastic cups, a mat or carpet, a timer, a tape measure."),
    h("2. Skit: Babel Construction Co. (your idea)"),
    p("I'm the foreman on the job site: \"Bricks up, slime on, we're making a NAME for ourselves!\" "
      "Halfway through, the workers draw cards and switch languages: auctioneer, Shakespeare, pirate, "
      "Cajun French, robot, sign language. A city inspector walks in at the end and shuts the job down."),
    p("**Needs:** 5-6 volunteers, the cards, about 5 min of script. Fits the 10 min with a short talk after."),
    h("3. Decoder race, one key split up (your idea)"),
    p("Each team gets the key verse in a different code: symbols, Morse, emoji, pigpen, backwards. "
      "But each team only has PART of the key, so they have to go find the other teams and trade. "
      "No team finishes alone. That's Babel backwards."),
    p("**Needs:** 5 printed code sheets + key pieces. I make them."),
    h("4. Google Translate telephone"),
    p("Before class I run Genesis 11:4 through 10 languages and back to English. Read the mangled "
      "version, they guess the verse. Short, quick laugh. Better as an opener than the main activity."),
    h("5. Back-to-back drawing"),
    p("Pairs sit back to back. One describes a tower picture, the other draws it. No shape words "
      "allowed (no square, circle, triangle). Compare drawings. Everybody plays at once."),
    h("6. Name bricks"),
    p("Every kid writes on a paper brick, no name: *one thing people our age build to make a name "
      "for ourselves* (followers, sports, grades, looks, being liked). Stack them into a tower on "
      "the table. Then knock it over, or leave it standing while I read Genesis 12:2. "
      "This could also be the object lesson INSIDE the lesson instead of the activity."),

    "<h2>Pick the BIG POINT for the lesson (about 15 min)</h2>",
    h("7. Making a name for ourselves"),
    p("Verse 4: *\"let us make us a name.\"* One chapter later God tells Abram *\"I will make "
      "thy name great.\"* At Babel they built their own name. With Abram, God gave it. "
      "Where do we try to build our own?"),
    scripture("Genesis 12:2"),
    h("8. God came down to see it"),
    p("Verse 5: they built a tower to reach heaven, and God still had to *come down* to see it. "
      "However big we build, it's small to Him."),
    h("9. Babel turned around: Pentecost"),
    p("At Babel, one language was split into many and people were scattered. At Pentecost, many "
      "languages heard one message and people were gathered. It ends in Revelation with every "
      "language together before the throne."),
    scripture("Acts 2:6"),
    scripture("Revelation 7:9"),
    h("10. Together is not always good"),
    p("They were united, one language, and working hard. But they were united *against* what God "
      "said (fill the earth, Genesis 9:1). A group that's all on the same page can still be on the "
      "wrong page. Fits teens and friend groups."),

    "<h2>Extras (add any)</h2>",
    "<h2>Fun facts (pick 1 or 2)</h2>",
    h("11. Fun fact: bricks with a name stamped on them"),
    funfact("They really did make a name on the bricks",
        "In the Bible, Babel and Babylon are the same word. Centuries later, King Nebuchadnezzar "
        "(the one from Daniel) rebuilt Babylon and stamped HIS NAME into the bricks. Archaeologists "
        "have dug up thousands of them, and museums have them today.",
        "Same city, same idea as verse 4, *\"let us make us a name.\"* And Nebuchadnezzar said it "
        "out loud in Daniel 4:30: *\"Is not this great Babylon, that I have built... by the might of "
        "my power, and for the honour of my majesty?\"* The next verse, God humbled him.",
        "*Honest note:* the stamped bricks are real, but they're from Nebuchadnezzar's time, long after "
        "the tower. Linking them to verse 4 is a connection, not something a verse says."),
    h("12. Fun fact: slime = tar, same stuff as Moses' basket"),
    funfact("Slime for morter",
        "Verse 3 *\"slime\"* is tar (bitumen) that bubbles up out of the ground in that part of the "
        "world. They had no stone, so they baked bricks and glued them with tar.",
        "The same word shows up when Moses' mother made his basket: *\"daubed it with slime and with "
        "pitch\"* (Exodus 2:3). Same stuff: at Babel it built a tower for man's name, on the Nile it "
        "saved the baby God would use."),
    h("13. Kids who speak another language"),
    p("If anybody speaks Spanish, Vietnamese, Cajun French (or has a grandparent who does), have them "
      "teach the class one phrase, like \"God loves you.\""),
    h("14. Candy questions (2 or 3)"),
    candy("a", "Why did they want to build the tower? Two reasons, both in verse 4.",
          "To make a name, and so they wouldn't be scattered."),
    candy("b", "They built it to reach heaven. What did God have to do to see it?",
          "Come down (verse 5)."),
    candy("c", "What would you do? Your friend group is all in on something you know is wrong. "
               "Everybody agrees. What do you do?",
          "EVERYONE who answers gets candy."),
    h("15. Closing: my story"),
    p("A time I tried to make a name for myself, or a time I went along with the group. "
      "Tell me which, and I'll help word it."),
]

out = os.path.join(HERE, "pdf")
os.makedirs(out, exist_ok=True)
for f in os.listdir(out):
    os.remove(os.path.join(out, f))
to_pdf(page(TITLE, "".join(body)), os.path.join(out, "1.4 Teacher - The Tower of Babel.pdf"))
FINAL = False
open(os.path.join(HERE, "index.html"), "w").write(web_page(
    os.path.basename(HERE), TITLE, "".join(body), [], final=FINAL))
mark = os.path.join(HERE, "FINAL")
if FINAL:
    open(mark, "w").close()
elif os.path.exists(mark):
    os.remove(mark)
print("done")
