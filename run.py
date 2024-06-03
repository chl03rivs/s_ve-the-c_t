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
alphabet = {(chr(ord(var)+i)) for i in range(26)}

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
    def __init__(self):
        self.lives_left = 9
        self.progress = progress_bar[0]
        self.setting = []    # will hold game mode and difficulty
        self.guesses = set()    # will contain the user's guesses

    def lose_life(self):
        self.lives_left -= 1
        
        print("Wrong answer! The cat has lost a life @__@ !!")
        return self.lives_left


class GameSettings:
    """
    Game mode and difficulty options
    Functions that will run in game_choice
    """
    def __init__(self):
        self.modes = ['mystery word', 'mystery sentence']
        self.diffs = ['easy', 'medium', 'hard']
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
    player = Player()

    player.progress = progress_bar[0]  # Set player's progress to 'intro'
    player.lives_left = 9  # Set player's initial lives to 9

    print(logo)
    print('Welcome to SAVE THE CAT! A terminal-based "hangman" game.')

    while True:
        skip = input("Do you want to read the rules? Y/N\n>>\n")

        if input_validation(player, skip):
            if skip in answer_yes:
                print(rules)
                print("Loading game...")
                print('...\n...\n...\n...\n...')
                game_choice(player)
                break
            elif skip in answer_no:
                print("Loading game...")
                print('...\n...\n...\n...\n...')
                game_choice(player)
                break

    return player    # return the instance so it can be used later


def game_choice(player):
    """
    Retrieves the game settings via user input
    The player is prompted to choose mode and difficulty
    """
    settings = GameSettings()

    print("Before we begin, you must choose the game mode & difficulty level.")
    print("Sentences will be harder than words.")
    print("Higher difficulties mean more letters to guess.")

    while True:
        player.progress = progress_bar[2]
        # choice of game mode
        print("Please choose a game mode by entering 1 or 2 on your keyboard.")
        print("Mystery Word: 1\nor\nMystery Sentence: 2")

        p_mode = input('>>\n')

        if input_validation(player, p_mode):
            game_mode = settings.choose_mode(p_mode)
            if game_mode:
                print("Choice saved.")
                break

    while True:
        player.progress = progress_bar[3]
        # choice of game difficulty
        print("Now, choose a game difficulty, please.")
        print("Easy: 1, \nMedium: 2, \nHard: 3")

        p_diff = input('>>\n')

        if input_validation(player, p_diff):
            game_diff = settings.choose_diff(p_diff)
            if game_diff:
                print("Choice saved.")
                break

    player.setting = [settings.game_mode, settings.game_diff]
    print(f"Loading a game with these settings: {player.setting}")
    print('...\n...\n...\n...\n...')
    get_user_guess(player)


def hangman_word(player):
    """
    Generates a random word
    Word length is based on player.setting
    """
    mystery_word = ''

    if player.setting == ['mystery word', 'easy']:
        mystery_word = wrd.word(word_min_length=3, word_max_length=5).upper()
    elif player.setting == ['mystery word', 'medium']:
        mystery_word = wrd.word(word_min_length=5, word_max_length=7).upper()
    elif player.setting == ['mystery word', 'hard']:
        mystery_word = wrd.word(word_min_length=8, word_max_length=12).upper()

    return mystery_word


def hangman_sentence(player):
    """
    Generates a random sentence
    Sentence complexity is based on player.setting
    """
    mystery_sentence = ''

    if player.setting == ['mystery sentence', 'easy']:
        mystery_sentence = s.bare_bone_sentence().upper()
    elif player.setting == ['mystery sentence', 'medium']:
        mystery_sentence = s.simple_sentence().upper()
    elif player.setting == ['mystery sentence', 'hard']:
        mystery_sentence = s.sentence().upper()

    return mystery_sentence


def get_user_guess(player):
    """
    Displays state of current mystery word/sentence

    Prompts the user's guess only while they have lives/guesses remaining
    Also handles validation of guess input
    """
    mystery = None   # initialize the variable
    if player.setting[0] == 'mystery word':
        mystery = hangman_word(player)
    elif player.setting[0] == 'mystery sentence':
        mystery = hangman_sentence(player)

    letters = set(mystery)
    current_mystery = [letter if letter in player.guesses
                       or letter == ' ' else '_' for letter in mystery]

    while player.lives_left > 0 and len(letters) > 0:
        print(f"You have {player.lives_left} lives left.\n")
        print(f"Previous guesses: {' '.join(player.guesses)}\n")
        print(drowning_cat[player.lives_left])

        print(f"The cat is anxious...\n{''.join(current_mystery)}")
        guess = input("Enter a guess:\n").upper()

        if guess in alphabet - player.guesses:
            player.guesses.add(guess)
        elif guess in player.guesses:
            print("Already guessed! Try a different letter please")
        else:
            print("Not a valid answer...\nPlease only use single letters!\n")
            continue

        if guess in letters:
            letters.remove(guess)
            print("Well done! You found a letter!\n")
        else:
            player.lose_life()

        current_mystery = [letter if letter in player.guesses
                           or letter == ' ' else '_' for letter in mystery]

    if len(letters) == 0:
        print(victory)
        player.progress = progress_bar[5]
        print(f"Congratulations!\nYou found all the letters:\n{mystery}")
    else:
        print(game_over)
        player.progress = progress_bar[6]
        print(f"Game Over...\nYou were so close :(")
        print(f"Your mystery was: {mystery}")

    replay(player)


def reset_game(player):
    """
    Handles the return to default in case of replay
    Sends the user back to the intro
    """
    player.lives_left = 9
    player.guesses = set()
    player.setting = []

    roll_intro()


def replay(player):
    """
    Prompts the user for a replay
    """
    player.progress = progress_bar[7]
    print("Would you like to play again? Y/N")

    while True:
        replay = input(">>\n")

        if input_validation(player, replay):
            if replay in answer_yes:
                print("Understood! Just a sec.")
                print("...")
                print("Turning back time...")
                print("...")
                print("...")
                reset_game(player)
                break
            elif replay in answer_no:
                print("Oh..\nOkay...")
                print("See you next time!")
                print("You can go now...")
                print("Bye...????")
                player.progress = progress_bar[8]
                break


def input_validation(player, value):
    """
    Validation and error handling function
    Checks user inputs based on where we are in the flowchart
    (using if statements with the progress attribute of the player class)
    """
    # for the yes/no questions
    if player.progress in [progress_bar[0], progress_bar[5],
                           progress_bar[6], progress_bar[7]]:
        try:
            if value not in answer_yes and value not in answer_no:
                raise ValueError(f"You must answer yes or no.\nYou entered {value}\n")
        except ValueError as e:
            print(f"Invalid data: {e}\nPlease try again.\n")
            return False
    elif player.progress in progress_bar[2]:    # for the game settings choices
        try:
            if (value != '1') and (value != '2'):
                raise ValueError(f"You must enter a number(1 or 2).\nYou entered {value}.")
        except ValueError as e:
            print(f"Invalid data: {e}\nPlease try again.\n")
            return False
    elif player.progress in progress_bar[3]:
        try:
            if (value != '1') and (value != '2') and (value != '3'):
                raise ValueError(f"You must enter a number (1, 2 or 3).\nYou entered {value}\n")
        except ValueError as e:
            print(f"Invalid data: {e}\nPlease try again.\n")
            return False
    return True


def main():
    """
    Runs the entire application
    """
    player = roll_intro()


main()
