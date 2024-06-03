# S_ve the c_t  

S_VE THE C_T is a terminal-based "hangman" game variation, with a dark(er) twist. 

To save the cat, the user has to guess a word/sentence, one letter at a time. Each mistake comes at a price...

**[View the live app here](https://save-the-cat-04e7dc8a4683.herokuapp.com)**

---
## Table of Contents
- [User Experience](#user-experience)
	- [Target audience](#target-audience)
	- [User Stories](#user-stories)
	- [App Aims](#app-aims)
- [Design](#design)
    - [Flowchart](#flowchart)
	- [App Structure](#app-structure)
	- [Imagery Used](#imagery-used)
- [Features](#features)
	- [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
	- [Code Validation](#code-validation)
	- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
	- [Bugs Fixed](#bugs-fixed)
	- [Known Bugs](#known-bugs)
- [Deployment steps](#deployment-steps)
	- [GitHub](#github)
	- [Cloning and forking](#cloning-and-forking)
-  [References & Acknowledgements](#references-and-acknowledgements)
	- [Sources](#sources)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements) 
---
## User Experience
Now, let's have a look at our target users and their needs!

### Target Audience
This game, in its current state, has a broad audience that it can appeal to. In order to play, you would need to know the letters of the alphabet, how to read/spell in English and use a computer.

Hangman is a game that most of us have played as a child. It is worth noting, however, that due to its gore/graphic theme, it may not be suited for young children. S_ve the c_t is no different and therefore, might be more suited for ages 7+.

### User Stories

**First-time user**
* I need an easy-to-understand introduction to the game and its rules
* I want to be able to choose the level of difficulty of the game
* I need to be aware of my life count
* I need to see a list of the guesses I have already made so I do not repeat them
* I need to receive clear feedback if I enter a wrong type of data and have a chance to try again without having to restart the game
* I need a clear indication if my guess was right or wrong
* I need to know when the game is started/over
* I want to be shown the correct answers if I game over
* I need to have the option to play again after a game if I want to

**Returning user**
*  I want to be able to skip the rules in the intro because I already know them
* I do not want to get the same mystery word or sentence to guess

### App Aims
The main goals of this app were as follows:

* to entertain the user;
* to challenge the user's vocabulary and patter recognition skills;
* to have straightforward, enjoyable interface and mechanics

---
##   Design  
Describe the design process briefly and the vibe you're going for

### Flowchart

### Imagery used 


----
## Features  
Hangman is a game in which players try to guess what letters are in a word before a complete picture of a man getting hanged appears. With each wrong guess, one element of the man (and the gruesome contraption that hangs him) is added.



In the features section you want to list all the features of your project. This is a great place to describe how each part of your site works. Its highly recommended to use screenshots here of all the features so the reader can 
easily identify the feature in question.


### Future Features
Here are a few of the ideas that I thought of while working on this project and may implement in the future, as I deepen my understanding of Python and broaden my programming skills.

**Quiz**
In order to make the game a bit more rewarding and educational, it would be interesting to have a higher difficulty level where we add a vocabulary check _after_ the user has guessed all the letters.

In this mode, victory can only be achieved by choosing the correct definition/synonym of the word.

Taking it up another notch, we could also have a level with a second language. Instead of simply being quizzed on the meaning of a word/sentence, we could be asked to translate it!

**Style the terminal**
In order to increase the replayability of the game and the user experience, I would like to implement a typing effect that would slow down the rate at which data is printed.

I looked into the possibility to trigger a screen clear using the OS module. Clearing the terminal after each stage of the game seems unpractical and also removes the option for the user to go over what was shared before.

Snce this did not satisfy my vision for the game, I want to look into other options to style the terminal and make it feel more like a conversation _with_ the user.

---
## Technologies used
This project was created using the [Python language](https://docs.python.org/3/).

---
## Testing  
describe testing plan and experience

### Code Validation 

### Manual testing  

---
## Bugs 
Bugs are an inherent part of the creative process that is programming. In Python, indentation plays a crucial role in determining scope and having an extra space in the wrong place can easily wreck the app flow.

One issue that surfaced while working on this project was related to the `get_user_guess` function. This function contains a loop that handles prompting the user for a guess while the user still has lives left.

The last component of this function is an _if statement_ that handles the victory/game over mechanics:

`if len(letters) == 0:
        print(victory)
        player.progress = progress_bar[5]
        print(f"Congratulations!\nYou found all the letters:\n{mystery}")
else:
    print(game_over)
    player.progress = progress_bar[6]
    print(f"Game Over...\nYou were so close :(")
    print(f"Your mystery was: {mystery}")`

A wrong indent was causing the game_over visuals to be printed to the terminal after every single wrong guess from the user. To fix it, I simply needed to remove this indent, so the statement would no longer be part of the loop.

----
## Deployment Steps
Github Pages was used to deploy this live website. 

### Heroku
The steps taken were as follows:

1. From your Heroku Dashboard, create an app
2. Once created, add two buildpacks from the _Settings_ tab. The ordering is as follows:
    1. `heroku/python`
    2. `heroku/nodejs`
3. Create a _Config Var_ called `PORT`. Set this to `8000`
4. From the _Deploy_ tab, you can then connect your GitHub account in the _Deployment method_ section.
5. Below that you will then be able to search for your repository and deploy your app.


### Cloning and forking
To view the cloning options available on Github:

1. Log in (or sign up) to [Github](https://github.com).
2. Find the repository for this project from [my profile](https://github.com/chl03rivs) in [night-owlzzz](https://github.com/chl03rivs).
3. Click on the blue **<> Code** button with the downward arrow.

If you wish to download a copy of this program and run it on your machine, you can do so  by choosing the **Download ZIP** options. Follow the usual steps of your machine to unzip the file and run it in your preferred software.

Note: your machine will need to have XX installed in order to run this project.

As this is a student project for the Code Institute Diploma in Full-Stack Development, forking is reserved to the assessment team. [GitHub documentation is available with the steps](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

----
## References & acknowledgments

Creativity and originality do not mean standing alone and figuring it all out on your own. Creative power is fuelled by community. So I am going to share the sources that helped me build the required knowledge for this project.

### Sources

**Documents consulted**

- cc
- etc.

**Tutorials referenced**

- 
-

**Other**


## Credits  
credit where credit is due

- who made the images
- any borrowed code, etc.

## Acknowledgements

As always, I want to thank Code Institute for the great learning materials they provided on XX, and my precious partner, Billy, for his undying love & support ♥
