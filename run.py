# module to generate random words and sentences
from wonderwords import RandomWord
from wonderwords import RandomSentence
# import ASCII art from visuals.py
from visuals import logo 
from visuals import drowning_cat 
from visuals import victory
from visuals import game_over 

# variables to use as shortcuts for wonderwords classes
wrd = RandomWord()
s = RandomSentence()

# lists that can be used when prompting user for a yes no question
# allows for variations of Y/N to be accepted	
answer_yes = ['yes', 'YES', 'y', 'Y', 'Yes','YEs','yeS','yeah']
answer_no = ['no','NO','N','n','No','nO','nah']

# creates a list of uppercase letters of the alphabet
# used to validate user guesses
var = 'A'
alphabet = [(chr(ord(var)+i)) for i in range(26)]

# dictionary holding the different game stages
progress_bar = {
    0: 'intro', 
    1: 'rules', 
    2: 'game choice', 
    3: 'guess', 
    4: 'victory', 
    5: 'game over', 
    6: 'replay',
    7: 'end'
}