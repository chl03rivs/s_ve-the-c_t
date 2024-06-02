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
answer_yes = ['yes', 'YES', 'y', 'Y', 'Yes', 'YEs', 'yeS', 'yeah']
answer_no = ['no', 'NO', 'N', 'n', 'No', 'nO', 'nah']

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

rules = """
         S_ve the c_t is a word guessing game.\n
         You must guess the mystery word/sentence to save the drowning cat!\n
         You can only guess one letter at a time.\n
         Each wrong guess will take one of your lives away.\n
         You only get 9 lives...\n
         So, choose carefully.
        """

class Player:
    """
    Player class to keep track of player status
    """
    full_health = 9
    lives_left = 9
    progress = progress_bar[0]
    setting = ()    # empty tuple that will hold game mode and difficulty
    guesses = []    # empty list to contain the user's guesses

    def lose_life(self):
        self.lives_left -= 1
        return self.lives_left
        print("Wrong answer! The cat has lost a life @__@ !!")


def roll_intro():
    """
    Provides the user with an intro of the game with logo
    and asks if they want to read the rules before proceding to game_choice()
    """
    Player.progress = progress_bar[0]

    print(logo)
    print('Welcome to SAVE THE CAT! A terminal-based "hangman" game.')

    while True:
        skip = input("Do you want to read the rules? Y/N\n>>\n")
    
        if input_validation(skip):
            if skip in answer_yes:
                print(rules)
            elif skip in answer_no:
                print("Loading game...")
                break


def input_validation(value):
    """
    Validation and error handling function
    Checks user inputs based on where we are in the flowchart
    (using if statements with the progress attribute of the Player class)
    """

    # for the yes/no questions
    if Player.progress in [progress_bar[0], progress_bar[4],
                           progress_bar[5], progress_bar[6]]:
        try:
            if value not in answer_yes and value not in answer_no:
                raise ValueError(f"You must answer yes or no.\nOnly {answer_yes} or {answer_no} are accepted.\nYou entered {value}.")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False
    elif Player.progress == progress_bar[2]:    # for the game settings choices
        try:
            if (value != '1') and (value != '2'):
                raise ValueError(f"You must enter a number.\nOnly 1 or 2 are accepted.\nYou entered {value}.")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False
    elif Player.progress == progress_bar[3]:
        try:
            if (value != '1') and (value != '2') and (value != '3'):
                raise ValueError(f"You must enter a number.\nOnly 1, 2 or 3 are accepted.\nYou entered {value}.")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False
    return True


roll_intro()
