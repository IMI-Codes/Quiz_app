from prompt_toolkit import print_formatted_text as print
from prompt_toolkit.formatted_text import FormattedText

welcome_message = FormattedText([("#000000","Welcome"),(""," "),("#FFFFFF","Player")])
print(welcome_message)
#Display "Welcome Player" 

"""
Display I take it you want to play 
Options :Yes or No 
"""

""" 
Yes Player wants to play
"""



#No player doesn't want to play

""" 
No Player doesn't want to play
Display So you Don't want to play\n Are you sure
Options Yes or No

Yes
Exit Game

No Go To Start Game
"""