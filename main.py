"""
Let me create a program that takes text
like "The quick brown fox jumped over the lazy dog" (representing a text that a person wants to memorize verbatim),
and returns a list of tuples (representing flashcards)
like the following:

Front: The ___
Back: quick

Front: quick ___
Back: brown

and so on.


options:
  length of underscore for replacing a word
  whether the underscore is fixed in length, or is exactly the same length as the word
  clue_length: number of words, or characters on the front of the card before the blank
  clue_type: whether the clue is in words, or characters
"""

from typing import List, Tuple

NON_FOCUS_BLANK = '___'
FOCUS_BLANK = '_?_'
FRONT_BACK_SEPARATOR = '$%$%'
BETWEEN_CARD_SEPARATOR = '*&*&'
NEW_LINE_SYMBOL = ' %NEW_LINE% '

def convert_single_line_text_to_flashcards(text: str) -> List[Tuple[str, str]]:
    original_text = text
    text = text.replace('\n', NEW_LINE_SYMBOL)
    words = text.split()
    i = 0
    results = []
    for word in words:
        if not words[i] == NEW_LINE_SYMBOL.strip():
            front_side, back_side =  quiz_on_nth_word(i, words)
        results.append((front_side, back_side))
        i += 1
        print(front_side, end='')
        print(FRONT_BACK_SEPARATOR, end='')
        print(back_side, end='')
        print(BETWEEN_CARD_SEPARATOR, end='')
    return results


def quiz_on_nth_word(n: int, words: List[str]) -> Tuple[str, str]:
    i = 0
    front_side = ''
    back_side = 'BLANK'
    for word in words:
        if word == NEW_LINE_SYMBOL.strip():
            front_side += '\n'
        elif i == n - 1:
            front_side += word + ' '
        elif i == n:
            front_side += FOCUS_BLANK + punctuation_at_end_of_word(word) + ' '
            back_side = word
        else:
            front_side += NON_FOCUS_BLANK + punctuation_at_end_of_word(word) + ' '

        i += 1
    return front_side, back_side


def punctuation_at_end_of_word(word: str):
    if word.endswith('.') or word.endswith(',') or word.endswith('!') or word.endswith('?'):
        return word[-1]
    else:
        return ''


convert_single_line_text_to_flashcards('Every day I walk home. \nI take a different road, today.')