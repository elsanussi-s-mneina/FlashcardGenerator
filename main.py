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
NEW_DOUBLE_LINE_SYMBOL = '%NEW_DOUBLE_LINE%'


def convert_single_line_text_to_word_by_word_flashcards(text: str) -> List[Tuple[str, str]]:
    text = text.replace('\n', NEW_LINE_SYMBOL)
    words = text.split()
    i = 0
    results = []
    for word in words:
        if not words[i] == NEW_LINE_SYMBOL.strip():
            front_side, back_side = quiz_on_nth_word(i, words)
            results.append((front_side, back_side))
            print(front_side, end='')
            print(FRONT_BACK_SEPARATOR, end='')
            print(back_side, end='')
            print(BETWEEN_CARD_SEPARATOR, end='')
        i += 1
    return results


def convert_single_line_text_to_line_by_line_flashcards(text: str) -> List[Tuple[str, str]]:
    text = text.replace('\n\n', NEW_DOUBLE_LINE_SYMBOL + '\n')
    lines = text.split('\n')
    i = 0
    results = []

    for line in lines:
        front_side, back_side = quiz_on_nth_line(i, lines)
        results.append((front_side, back_side))
        print(front_side, end='')
        print(FRONT_BACK_SEPARATOR, end='')
        print(back_side, end='')
        print(BETWEEN_CARD_SEPARATOR, end='')
        i += 1
    return results


def quiz_on_nth_word(n: int, words: List[str]) -> Tuple[str, str]:
    i = 0
    front_side = ''
    back_side = 'BLANK'
    previous_word = ''
    for word in words:
        if is_new_line_symbol(word):
            front_side += '\n'
        elif i == n - 1 or (i == n - 2 and next_word_is_new_line(words, i)):
            front_side += word + ' '
        elif i == n:
            front_side += FOCUS_BLANK + punctuation_at_end_of_word(word) + ' '
            back_side = strip_punctuation_on_end(word)
        else:
            front_side += NON_FOCUS_BLANK + punctuation_at_end_of_word(word) + ' '
        i += 1
        previous_word = word
    return front_side, back_side


def quiz_on_nth_line(n: int, lines: List[str], long_version=False) -> Tuple[str, str]:
    i = 0
    front_side = ''
    back_side = ''
    for line in lines:
        if i == n - 1:
            front_side += line + '\n'
        elif i == n:
            front_side += str(i + 1) + ') ' + '____?_____'
            back_side = line
        elif long_version:
            front_side += '__________\n'
        i += 1
    front_side = front_side.replace(NEW_DOUBLE_LINE_SYMBOL, '\n')
    back_side = back_side.replace(NEW_DOUBLE_LINE_SYMBOL, '\n')
    return front_side, back_side


def next_word_is_new_line(words: List[str], index: int) -> bool:
    return is_new_line_symbol(words[index + 1])


def is_new_line_symbol(token: str) -> bool:
    return token == NEW_LINE_SYMBOL.strip()


def is_new_double_line_symbol(token: str) -> bool:
    return token == NEW_DOUBLE_LINE_SYMBOL.strip()


def punctuation_at_end_of_word(word: str) -> str:
    if word.endswith('.') or word.endswith(',') or word.endswith('!') or word.endswith('?'):
        return word[-1]
    else:
        return ''


def strip_punctuation_on_end(word: str) -> str:
    if word.endswith('.') or word.endswith(',') or word.endswith('!') or word.endswith('?'):
        return word[:-1]
    else:
        return word