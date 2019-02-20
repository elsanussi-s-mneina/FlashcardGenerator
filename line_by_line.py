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
    flashcards = convert_text_to_line_by_line_flashcards(text, blind_blank=blind_blank)
    csv_text = convert_flashcards_to_csv_text(flashcards)
    return csv_text


def convert_text_to_line_by_line_flashcards(text: str, blind_blank=True) -> List[Tuple[str, str]]:
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
    i = 0
    front_side = ''
    back_side = ''
    for line in lines:
        line = line.replace(NEW_DOUBLE_LINE_SYMBOL, '\n')
        if i == n - 1:
            front_side += line + '\n'
        elif i == n:
            if blind_blank:
                front_side += str(i + 1) + ') ' + LINE_FOCUS_BLANK
            else:
                front_side += str(i + 1) + ') ' + custom_blank_line_with_spaces_between_words_shown(line)
            back_side = line
        elif long_version:
            front_side += LINE_NON_FOCUS_BLANK + '\n'
        i += 1
    front_side = front_side.replace(NEW_DOUBLE_LINE_SYMBOL, '\n')
    back_side = back_side.replace(NEW_DOUBLE_LINE_SYMBOL, '\n')
    return front_side.rstrip(), back_side.rstrip()


def custom_blank_line_with_spaces_between_words_shown(line: str):
    return re.sub(r'\w', '_', line)
