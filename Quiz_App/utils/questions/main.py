#cleaning up the questions
import json
"""
Sort By Topic
Sort By Difficulty
Sort By Question Type
"""

fhand = open("questions_2.json",encoding='utf-8')

content  = fhand.read().encode("utf-8",errors='replace') # type: ignore
questions = json.loads(content)
anime = open("anime.json","x")
tech = open("tech.json","x")
for question in questions:
  if question["topic"] == "anime":
    json.dump(question,anime)
    del question
  elif question["topic"] == "tech":
    json.dump(question,tech)
    del question