from prompt_toolkit import print_formatted_text as s_print
from prompt_toolkit import prompt

s_print("Welcome Player")

message = "What is your Name?\n"

name = prompt(message)
print(name)