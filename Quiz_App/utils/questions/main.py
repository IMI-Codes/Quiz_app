#cleaning up the questions
import json
"""
Sort By Topic
Sort By Difficulty
Sort By Question Type
"""

with open("questions_2.json") as f:
  data = json.load(f)
for value in data:
  print(value) 