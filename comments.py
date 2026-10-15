#!/usr/bin/env python3
"""Read or clear Andrew's ✎ notes on the Sunday school lesson pages.
   python3 comments.py         print them, by lesson
   python3 comments.py clear   archive to notes-archive.jsonl, then wipe
The key is NOT in this (public) repo: it is the book site's key + "-ss"."""
import json, os, pathlib, sys, time, urllib.request
KEY = (pathlib.Path.home() / "Development/while-you-live/notes/comment-key.txt").read_text().strip() + "-ss"
URL = "https://api.jobhubgo.com/api/yam/" + KEY
ARCHIVE = pathlib.Path.home() / "Development/while-you-live/notes/sunday-school-notes-archive.jsonl"
d = json.load(urllib.request.urlopen(URL)).get("data") or {}
cs = d.get("comments", [])
if sys.argv[1:] == ["clear"]:
    with open(ARCHIVE, "a") as f:
        for c in cs:
            f.write(json.dumps(dict(c, cleared=time.strftime("%Y-%m-%dT%H:%M"))) + "\n")
    body = json.dumps({"data": {"comments": []}, "updatedAt": int(time.time() * 1000)}).encode()
    req = urllib.request.Request(URL, body, {"Content-Type": "application/json"}, method="PUT")
    print(urllib.request.urlopen(req).read().decode())
else:
    print(f"{len(cs)} note(s)")
    for c in sorted(cs, key=lambda c: (c["lesson"], c["i"], c["at"])):
        print(f'\n{c["lesson"]}  block {c["i"]}  [{c["at"][:16]}]\n  "{c["quote"]}"\n  -> {c["text"]}')
