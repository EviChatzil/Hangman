# __A SIMPLE HANGMAN GAME__

#### Video Demo:  <https://www.youtube.com/watch?v=4YI6CHY4j8k>

## __Description__:

This is a final project for the CS50P course by Harvard.

---------------------------------------------------------------
### __Libraries__

- [random](https://docs.python.org/3/library/random.html)
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

### __How to start__

Initially, to play this game, run:
```
    pip install -r requirements.txt
    python hangman.py
```

This is a simple hangman game.

### __Usage__

As the progrmam starts it randomly chooses a word from a file, it displays the word with underscores instead of letters and asks you to make a guess or type the word "hint", in order to get help. The player has 6 tries to guess a letter and can ask for help 2 times. The remaining tries, hints, the missed letters and an optimization of the hangman are being displayed.

```
Welcome to Hangman!
You have 6 shots to find the word.
Let's start!
Word:  _ _ _ _ _
Shots: 6
Hints: 2
No missed letters yet.

        ______
        |    |
             |
             |
             |

Guess a letter or type 'hint' to get help:

```
If the player inputs one letter, firstly it is being checked if the word contains this letter. If this is the case, the word is being displayed with the letter appearing and underscores in the positions of the other letters. If the word doesn't contain the letter, the number of shots decreases by 1 and a new hangman picture is being presented.

If the player types 'hint', the word is being displayed with a random letter appearing. The number of hints decreases by 1.

If the player doesn't type as a guess just one letter or doesn't type an aplhabetical character, the player is being asked again for a correct input.

If the player manages to find the word, the following is being displayed:
```
Correct guess!
Congratulations! You've guessed the word: t r o u b l e .

```

If the player doesn't manage to find the word, the word is being revealed along with a definition from merriam webster dictionary:
```
Game Over! You missed it!
The word was t h r o w
Here is a definition:  to propel through the air by a forward motion of the hand and arm

```
### __Functions__

#### __create_list() function__
Function that creates a list of words from a txt file.

#### __choose_word() function__
Function that returns a random word from a list.

#### __hangman_pic() function__
Function that takes as argument the missed letters and returns the equivalent hangman picture.

#### __display_word() function__
Function that takes as arguments the word to guess, the guessed letters and the hint(s), and displays the word with the guessed letters and the hints appearing and the rest positions with '_'.

#### __hint() function__
Function that takes as arguments the word, the guessed letters and the (possible) previous hint, and returns a new hint.

#### __get_def() function__
Function that takes a word as argument and returns the first definition of merriam webster dictionary.


