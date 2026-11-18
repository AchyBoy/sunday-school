import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from lib import *

# ROUND 1 = an IDEA MENU, every idea numbered so he can say "I like 3, tweak 7".
# He doesn't have the book with him, so everything sits on Genesis 11:1-9 itself.
TITLE = "Lesson 1.5: The Tower of Babel"
B = "📘 "  # from the book

body = [
    f"<h1>{TITLE}</h1>",
    '<div class="sub">Genesis 11:1-9 · Proverbs 16:18-19 · James 4:6-10 · Ages 14-17, about 30 kids · '
    "Lesson about 15 min + activity about 10 min</div>",
    '<div class="sub">Book: <b>God resists the proud and arrogant.</b> '
    "Big idea: <b>I will worship only the one true God.</b></div>",
    note("**Idea menu, round 2: the book is in.** 📘 = from the book. Every idea has a number. "
         "Tap ✎ on any of them: keep it, cut it, or tell me what to change. Then I build the final lesson."),

    h("The passage"),
    scripture("Genesis 11:1-9"),

    "<h2>Pick ONE activity (about 10 min)</h2>",
    h("1. Silent tower build"),
    p("Teams of 6 race to build the tallest tower out of cups or index cards and tape, 3 minutes. "
      "At 90 seconds every kid gets a secret card: *only talk in questions · only Spanish · "
      "no talking, only humming · every sentence starts with \"Banana\" · disagree with the last "
      "person who spoke.* The towers fall apart. The lesson shows itself."),
    p("**Needs:** about 150 cups or 5 packs of index cards + tape, 30 printed cards."),
    h("2. Boys build a human pyramid, girls stack cups (your idea)"),
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
    p("**Ties to the book:** the team that goes up too early, too proud, falls. "
      "*\"Pride goeth before destruction, and an haughty spirit before a fall.\"*"),
    p("**Needs:** about 150 plastic cups, a mat or carpet, a timer, a tape measure."),
    h("3. Skit: Babel Construction Co. (your idea)"),
    p("I'm the foreman on the job site: \"Bricks up, slime on, we're making a NAME for ourselves!\" "
      "Halfway through, the workers draw cards and switch languages: auctioneer, Shakespeare, pirate, "
      "Cajun French, robot, sign language. A city inspector walks in at the end and shuts the job down."),
    p("**Needs:** 5-6 volunteers, the cards, about 5 min of script."),
    h("4. Decoder race, one key split up (your idea)"),
    p("Each team gets the key verse in a different code: symbols, Morse, emoji, pigpen, backwards. "
      "But each team only has PART of the key, so they have to go find the other teams and trade. "
      "No team finishes alone. Key verse could be James 4:6 to match the book."),
    p("**Needs:** 5 printed code sheets + key pieces. I make them."),
    h(B + "5. Alphabet ball toss, then backwards"),
    p("Two lines, a small ball. Each person says the next letter (A, B, C...) and tosses it on. "
      "Drop it, start over. Time each team. Then do it BACKWARDS (Z, Y, X...). "
      "Book's point: overconfidence leaves us unprepared, humility prepares us. Only about 5 min, "
      "so it could pair with something."),
    p("**Needs:** 2 small balls, a timer."),
    h(B + "6. True or false world records"),
    p("I read 10 world records, 5 real and 5 made up, and they vote true or false. "
      "Book's point: people will do strange things to make a name. I'll find 5 real ones if you pick it."),
    h("7. Google Translate telephone"),
    p("Genesis 11:4 run through 10 languages and back to English. They guess the verse. Quick opener."),
    h("8. Back-to-back drawing"),
    p("Pairs back to back. One describes a tower picture, the other draws it. No shape words."),

    "<h2>The lesson (about 15 min). The book's point is PRIDE.</h2>",
    h(B + "9. God resists the proud"),
    p("The book's main point. The tower was pride: *\"let us make us a name.\"* God fights against pride. "
      "If I let pride in, I'm asking God to fight me, and that's not a fight I win."),
    scripture("James 4:6"),
    scripture("Proverbs 16:18-19"),
    h("10. Making a name for ourselves"),
    p("Verse 4: *\"let us make us a name.\"* One chapter later God tells Abram *\"I will make thy name "
      "great.\"* At Babel they built their own name. With Abram, God gave it. "
      "Can be done with **name bricks:** every kid writes on a paper brick, no name, one thing people "
      "our age do to make a name (followers, sports, grades, looks). Stack them, then knock them over."),
    scripture("Genesis 12:2"),
    h(B + "11. Pride hides in little ways"),
    p("Most of us would never tell God \"I'm right and You're wrong.\" But we say it without words: "
      "a day with no prayer, a week with no Bible, a big decision without asking God. "
      "And false confidence: skipping the study guide, the parking spot that was too small."),
    h(B + "12. Humble yourselves, and He lifts you up"),
    p("They tried to build their way UP to heaven. James says get low, and God lifts you up. "
      "Humility is not putting yourself down. It's lifting Jesus higher, getting off the throne and "
      "putting Him on it. Book's commitment: *I will worship only the one true God.*"),
    scripture("James 4:7-10"),
    h(B + "13. The quicksand story"),
    p("A man is stuck in quicksand. Confucius says he should stay out of places like this. Buddha says let "
      "it be a lesson to the world. Mohammad says it is the will of God. Jesus says: \"Take my hand, I will "
      "save you.\" Only Jesus actually helps. *The book calls it a legend, it's a made-up story, so I'd say that too.*"),
    h("14. Babel turned around: Pentecost"),
    p("Babel: one language split, people scattered. Pentecost: many languages heard one message, people "
      "gathered. Revelation: every language together before the throne."),
    scripture("Acts 2:6"),
    scripture("Revelation 7:9"),
    h("15. God came down to see it"),
    p("Verse 5: they built a tower to reach heaven, and God still had to *come down* to see it."),
    h(B + "16. Together is not always good"),
    p("They were united and working hard, but against what God said: spread out and fill the earth. "
      "A group all on the same page can still be on the wrong page. The book says this too."),
    scripture("Genesis 9:1"),
    h(B + "17. Opener: famous for no reason"),
    p("The book opens with Vine and Thomas Sanders. **Honest note:** Vine shut down in 2017, when these "
      "kids were 5 to 8, so most won't know it. Same question works with today's apps: "
      "*can you think of someone who is popular for no reason at all?*"),

    "<h2>Fun facts (pick 1 or 2)</h2>",
    h("18. Fun fact: bricks with a name stamped on them"),
    funfact("They really did make a name on the bricks",
        "In the Bible, Babel and Babylon are the same word. Centuries later, King Nebuchadnezzar "
        "(the one from Daniel) rebuilt Babylon and stamped HIS NAME into the bricks. Archaeologists "
        "have dug up thousands of them, and museums have them today.",
        "Same city, same idea as verse 4, *\"let us make us a name.\"* And Nebuchadnezzar said it "
        "out loud in Daniel 4:30: *\"Is not this great Babylon, that I have built... by the might of "
        "my power, and for the honour of my majesty?\"* The next verse, God humbled him.",
        "*Honest note:* the stamped bricks are real, but they're from Nebuchadnezzar's time, long after "
        "the tower. Linking them to verse 4 is a connection, not something a verse says."),
    h("19. Fun fact: slime = tar, same stuff as Moses' basket"),
    funfact("Slime for morter",
        "Verse 3 *\"slime\"* is tar (bitumen) that bubbles up out of the ground in that part of the "
        "world. They had no stone, so they baked bricks and glued them with tar.",
        "The same word shows up when Moses' mother made his basket: *\"daubed it with slime and with "
        "pitch\"* (Exodus 2:3). Same stuff: at Babel it built a tower for man's name, on the Nile it "
        "saved the baby God would use."),
    "<h2>Extras (add any)</h2>",
    h("20. Kids who speak another language"),
    p("If anybody speaks Spanish, Vietnamese, Cajun French (or has a grandparent who does), have them "
      "teach the class one phrase, like \"God loves you.\""),
    h("21. Candy questions (2 or 3)"),
    candy("a", "Why did they want to build the tower? Two reasons, both in verse 4.",
          "To make a name, and so they wouldn't be scattered."),
    candy("b", "Finish it: Pride goeth before destruction, and an haughty spirit before a...",
          "Fall (Proverbs 16:18). Good right after the towers fall."),
    candy("c", "What would you do? Your friend group is all in on something you know is wrong. "
               "Everybody agrees. What do you do?",
          "EVERYONE who answers gets candy."),
    h("22. Closing: my story"),
    p("A time I tried to make a name for myself, or a time I went along with the group. "
      "Tell me which, and I'll help word it."),
]

out = os.path.join(HERE, "pdf")
os.makedirs(out, exist_ok=True)
for f in os.listdir(out):
    os.remove(os.path.join(out, f))
to_pdf(page(TITLE, "".join(body)), os.path.join(out, "1.5 Teacher - The Tower of Babel.pdf"))
FINAL = False
open(os.path.join(HERE, "index.html"), "w").write(web_page(
    os.path.basename(HERE), TITLE, "".join(body), [], final=FINAL))
mark = os.path.join(HERE, "FINAL")
if FINAL:
    open(mark, "w").close()
elif os.path.exists(mark):
    os.remove(mark)
print("done")
