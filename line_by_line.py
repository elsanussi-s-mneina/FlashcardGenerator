from typing import List, Tuple
import re

from card_separation_tokens import convert_flashcards_to_csv_text

NEW_DOUBLE_LINE_SYMBOL = '%NEW_DOUBLE_LINE%'
LINE_FOCUS_BLANK = '_____?_____'
LINE_NON_FOCUS_BLANK = '___________'


def print_text_to_line_by_line_flashcards_csv(text: str, blind_blank=True):
    csv_text = convert_text_to_flashcards_as_csv(text, blind_blank=blind_blank)
    print(csv_text)


def convert_text_to_flashcards_as_csv(text: str, blind_blank=True) -> str:
    """
    :param text: the text to be memorized
    :param blind_blank: whether a line is replaced by a single blank instead of a blank per word
    :return: a string representing a deck of flashcards as special separated values. These may be imported
    by software that supports importing comma-separated values file while setting a different
    column and row separator.
    I usually just past this string into Quizlet's import webpage.
    """
    flashcards = convert_text_to_line_by_line_flashcards(text, blind_blank=blind_blank)
    csv_text = convert_flashcards_to_csv_text(flashcards)
    return csv_text


def convert_text_to_line_by_line_flashcards(text: str, blind_blank=True) -> List[Tuple[str, str]]:
    """

    :param text: the text the user is trying to memorize.
    :param blind_blank: whether a line is replaced by a single blank instead of a blank per word
    that has the same number of characters as the word's in it or not.
    i.e. whether "first second third" is replaced by "_____?_____" or the easier "_?_ _?_ _?_".
    :return: flashcards. Each flashcard consists of a front side and a back side. The front
    side contains part of the text with part of it missing, the back side contains the part
    that the learner needs to recall.
    """
    text = text.replace('\n\n', NEW_DOUBLE_LINE_SYMBOL + '\n')
    lines = text.split('\n')
    i = 0
    results = []

    for _ in lines:
        front_side, back_side = quiz_on_nth_line(i, lines, blind_blank=blind_blank)
        results.append((front_side, back_side))
        i += 1
    return results


def quiz_on_nth_line(n: int, lines: List[str], long_version=False, blind_blank=True) -> Tuple[str, str]:
    """
    This will return a flashcard for memorizing a single line.
    :param n: a number that indicates which line is the target of memorization.
    :param lines: lines of text to be learnt. (the text to be memorized after it is split into lines)
    :param long_version: whether to include blank lines for the lines that are part of the text
    but are not currently being memorized and are not part of the hint.
    :param blind_blank: whether a line is replaced by a single blank instead of a blank per word
    :return: a single flashcard, that is, a front side and a back side.
    """
    i = 0
    front_side = ''
    back_side = ''
    for line in lines:
        line = line.replace(NEW_DOUBLE_LINE_SYMBOL, '\n')
        if i == n - 1:
            front_side += line + '\n'
        elif i == n:
            if blind_blank:
                front_side += line_label(i) + LINE_FOCUS_BLANK
            else:
                front_side += line_label(i) + custom_blank_line_with_spaces_between_words_shown(line)
            back_side = line
        elif long_version:
            front_side += LINE_NON_FOCUS_BLANK + '\n'
        i += 1
    front_side = front_side.replace(NEW_DOUBLE_LINE_SYMBOL, '\n')
    back_side = back_side.replace(NEW_DOUBLE_LINE_SYMBOL, '\n')
    return front_side.rstrip(), back_side.rstrip()


def custom_blank_line_with_spaces_between_words_shown(line: str) -> str:
    """
    Replace all alphabetic characters with underscore characters.
    For example "This thing" would become "____ _____".
    :param line: a line of text
    :return: a line of text
     """
    return re.sub(r'\w', '_', line)


def line_label(line_number: int) -> str:
    """
    Labels a line with a number. This is useful
    when a flashcard only contains an excerpt of the
    full text to be memorized. It allows a hint of context.

    :param line_number: For the first line pass in zero.
    """
    return str(line_number + 1) + ') '
