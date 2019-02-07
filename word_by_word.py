from typing import List, Tuple

from card_separation_tokens import convert_flashcards_to_csv_text

FOCUS_BLANK = '_?_'
NON_FOCUS_BLANK = '___'
NEW_LINE_SYMBOL = ' %NEW_LINE% '


def print_single_line_text_to_word_by_word_flashcards_csv(text: str):
    csv_text = convert_text_to_flashcards_as_csv(text)
    print(csv_text)


def convert_text_to_flashcards_as_csv(text: str) -> str:
    flashcards = convert_single_line_text_to_word_by_word_flashcards(text)
    csv_text = convert_flashcards_to_csv_text(flashcards)
    return csv_text


def convert_single_line_text_to_word_by_word_flashcards(text: str) -> List[Tuple[str, str]]:
    text = text.replace('\n', NEW_LINE_SYMBOL)
    words = text.split()
    i = 0
    results = []
    for word in words:
        if not words[i] == NEW_LINE_SYMBOL.strip():
            front_side, back_side = quiz_on_nth_word(i, words)
            results.append((front_side, back_side))
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


def quiz_on_nth_word_show_all_previous_words(n: int, words: List[str]) -> Tuple[str, str]:
    i = 0
    front_side = ''
    back_side = 'BLANK'
    for word in words:
        if is_new_line_symbol(word):
            front_side += '\n'
        elif i < n:
            front_side += word + ' '
        elif i == n:
            front_side += FOCUS_BLANK + punctuation_at_end_of_word(word) + ' '
            back_side = strip_punctuation_on_end(word)
        else:
            front_side += NON_FOCUS_BLANK + punctuation_at_end_of_word(word) + ' '
        i += 1
    return front_side, back_side


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


def next_word_is_new_line(words: List[str], index: int) -> bool:
    return is_new_line_symbol(words[index + 1])


def is_new_line_symbol(token: str) -> bool:
    return token == NEW_LINE_SYMBOL.strip()
