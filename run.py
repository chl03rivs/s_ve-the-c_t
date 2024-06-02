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
    2: 'game mode choice',
    3: 'game diff choice',
    4: 'guess',
    5: 'victory',
    6: 'game over',
    7: 'replay',
    8: 'end'
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

class GameSettings:
    """
    Game mode and difficulty options
    Functions that will run in game_choice
    """
    def __init__(self):
        self.modes = ['mystery word', 'mystery sentence']
        self.diffs = ['easy','medium','hard']
        self.game_mode = ''
        self.game_diff = ''

    def choose_mode(self, value):
        if value == '1':
            self.game_mode = self.modes[0]
        elif value == '2':
            self.game_mode = self.modes[1]

        print(f"You have chosen the {self.game_mode} game mode!")
        return self.game_mode
    
    def choose_diff(self, value):
        if value == '1':
            self.game_diff = self.diffs[0]
        elif value == '2':
            self.game_diff = self.diffs[1]
        elif value == '3':
            self.game_diff = self.diffs[2]
        
        print(f"You have chosen the {self.game_diff} difficulty!")
        return self.game_diff


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
                break
                print("Loading game...")
            elif skip in answer_no:
                print("Loading game...")
                break


def game_choice():
    """
    Retrieves the game settings via user input
    Player is prompted to choose mode and difficulty
    """
    settings = GameSettings()

    print("Before we begin, you must choose the game mode & difficulty level.\nThe higher the level the more letters you will have to guess before the cat drowns!")

    while True:
        Player.progress = progress_bar[2]
        # choice of game mode
        print("Please choose a game mode by entering 1 or 2 on your keyboard:\nMystery Word [1]\nor\nMystery Sentence [2]")

        p_mode = input('>> ')

        if input_validation(p_mode):
            game_mode = settings.choose_mode(p_mode)
            if game_mode:
                print("Choice saved.")
                break
    
    while True:
        Player.progress = progress_bar[3]
        # choice of game difficulty
        print("Please choose a game difficulty by entering 1, 2 or 3 on your keyboard:\nEasy[1],\nMedium[2],\nHard[3]")

        p_diff = input('>> ')

        if input_validation(p_diff):
            game_diff = settings.choose_diff(p_diff)
            if game_diff:
                print("Choice saved.")
                break


    Player.setting = (settings.game_mode, settings.game_diff)
    print(f"You are now proceding into\na game with these settings: {Player.setting}")


def input_validation(value):
    """
    Validation and error handling function
    Checks user inputs based on where we are in the flowchart
    (using if statements with the progress attribute of the Player class)
    """
    # for the yes/no questions
    if Player.progress in [progress_bar[0], progress_bar[5],
                           progress_bar[6], progress_bar[7]]:
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


def main():
    """
    Runs the entire application
    """
    roll_intro()
    game_choice()

main()