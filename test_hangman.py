from project import choose_word, hangman_pic, display_word, hint, get_def
import random
import pytest

def main():
    test_hangman_pic()
    test_display_word()
    test_get_def()
    test_choose_word()
    test_hint()

@pytest.fixture(autouse=True)
def set_random_seed():
    random.seed(1)

def sample_words():
    return["apple", "lazy", "carrot"]

def test_choose_word():
    word = choose_word(sample_words())
    expected_word = "apple"
    assert word == expected_word

def test_hint():
    assert hint("apple") == "a"
    assert hint("lazy") == "l"
    assert hint("apple", ["a"]) == "p"

def test_hangman_pic():
    assert hangman_pic(3) == """
        ______
        |    |
        O    |
       /|    |
             |
    """


def test_display_word():
    assert display_word("player", [], []) == "_ _ _ _ _ _ "
    assert display_word("player", ['p', 'a'], []) == "p _ a _ _ _ "
    assert display_word("player", ['l'], ['r']) == "_ l _ _ _ r "
    assert display_word("player", [], ['r']) == "_ _ _ _ _ r "


def test_hint():
    assert hint("apple", []) == 'p'
    assert hint("apple", ['a']) == 'p'
    assert hint("apple", ['p']) == 'l'

def test_get_def():
    assert get_def("resort") == "one that affords aid or refuge "

if __name__ == "__main__" :
    main()