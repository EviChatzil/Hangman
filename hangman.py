import random
import requests
from bs4 import BeautifulSoup

#Function that creates a list of words from a txt file
def create_list(file_name):
    with open(file_name) as f:
        list_of_words = f.read().splitlines()
        list_no_doubles = []
        for word in list_of_words:
            if word not in list_no_doubles:
                list_no_doubles.append(word)
        return list_no_doubles

#Function that returns a random word from a list
def choose_word(list_of_words):
    return random.choice(list_of_words)

#Function that takes as argument the missed letters and returns a hangman picture
def hangman_pic(missed_letters):
    pics = [
    """
        ______
        |    |
             |
             |
             |
    """,
    """
        ______
        |    |
        O    |
             |
             |
    """,
    """
        ______
        |    |
        O    |
        |    |
             |
    """,
    """
        ______
        |    |
        O    |
       /|    |
             |
    """,
    """
        ______
        |    |
        O    |
       /|\   |
             |
    """,
    """
       ______
       |    |
       O    |
      /|\   |
      /     |
    """,
    """
        ______
        |    |
        O    |
       /|\   |
       / \   |
    """
    ]

    return pics[missed_letters]

#Function that takes as arguments the word to guess, the guessed letters and the hint(s) and displays the word
#with the guessed letters and the hints appearing and the rest positions with '_'
def display_word(word, guessed_letters, hints):
    display = ""
    for letter in word:
        if letter in guessed_letters or letter in hints:
            display += f"{letter} "
        else:
            display += "_ "
    return display

#Function that takes as arguments the word, the guessed letters and the (possible) previous hint and returns a new hint
def hint(word, guessed_letters):
    hint = random.randint(1, len(word)-1)
    while word[hint] in guessed_letters:
        hint = random.randint(1, len(word) - 1)
    return(word[hint])

#Function that takes a word as argument and returns the first definition of merriam webster dictionary
def get_def(word):

    url = f"https://www.merriam-webster.com/dictionary/{word}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    definition = soup.find(class_="dtText")

    definition = definition.text.lstrip(": ").rstrip(":")
    if ":" in definition:
        a, b = definition.split(":")
        return a
    else:
        return definition

def main():
    #Create the word to guess variable using the choose_word function
    word_list = create_list("words.txt")
    word_to_guess = choose_word(word_list)
    #Create the variable guessed_letters, missed_letter, shots, hints, hint_count
    guessed_letters = []
    missed_letters = []
    shots = 6
    hints = []
    hint_count = 2
    print("Welcome to Hangman!")
    print("You have 6 shots to find the word.")
    print("Let's start!")

    while shots > 0:
        #Call display function and assign it to a variable
        display = display_word(word_to_guess, guessed_letters, hints)
        print("Word: ", display)
        print(f"Shots: {shots}")
        print(f"Hints: {hint_count}")

        #Print missed letters
        if len(missed_letters) == 0:
            print("No missed letters yet.")
        elif len(missed_letters) != 0:
            print("Missed letters: ", end="")
            for missed_letter in missed_letters:
                print(f"{missed_letter} ", end="")
            print()

        #Print the correct hangman_pic according to the length of missed_letters list
        print(hangman_pic(len(missed_letters)))

        #Ask the player to type a letter or 'hint'
        guess = input("Guess a letter or type 'hint' to get help: ").lower()

        #case hint: find the hint_letter using the hint function, append the hint_letter to the hints list and to the
        #guessed_letters list, deduct one try from the players hint_count, if the player hasn't used his 2 tries yet
        if guess == "hint" and hint_count > 0:
            hint_letter = hint(word_to_guess, guessed_letters)
            hints.append(hint_letter)
            guessed_letters.append(hint_letter)
            hint_count -= 1
            continue
        elif guess == "hint" and hint_count <= 0:
            print("All the hints have been used.")
            continue

        #Check if the player types only 1 alphabetical character
        if len(guess) != 1 or not guess.isalpha():
            print("Just one letter!")
            continue

        #Check if the letter, that the player types, is already guessed
        if guess in guessed_letters or guess in missed_letters:
            print("Letter already guessed or taken as hint!")
            continue

        #Case the guess is correct
        if guess in word_to_guess:
            guessed_letters.append(guess)
            print("Correct guess!")
            #Check if the word is found
            if set(word_to_guess) == set(guessed_letters):
                print("Congratulations! You've guessed the word:", (" ").join(word_to_guess), ".")
                break
        #Case the guess is not correct
        else:
            print("Wrong guess. Try again!")
            if guess not in missed_letters:
                missed_letters.append(guess)
            print(hangman_pic(len(missed_letters)))
            shots -= 1

        #Check GAME OVER
        if shots == 0:
            print("Game Over! You missed it!")
            x = " ".join(word_to_guess)
            print(f"The word was {x}")
            print("Here is a definition: ", get_def(word_to_guess))
            break

if __name__ == "__main__" :
    main()