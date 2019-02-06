from typing import List, Tuple

from card_separation_tokens import convert_flashcards_to_csv_text

NEW_DOUBLE_LINE_SYMBOL = '%NEW_DOUBLE_LINE%'
LINE_FOCUS_BLANK = '_____?_____'
LINE_NON_FOCUS_BLANK = '___________'


def print_single_line_text_to_line_by_line_flashcards_csv(text: str):
    csv_text = convert_text_to_flashcards_as_csv(text)
    print(csv_text)


def convert_text_to_flashcards_as_csv(text: str) -> str:
    flashcards = convert_single_line_text_to_line_by_line_flashcards(text)
    csv_text = convert_flashcards_to_csv_text(flashcards)
    return csv_text


def convert_single_line_text_to_line_by_line_flashcards(text: str) -> List[Tuple[str, str]]:
    text = text.replace('\n\n', NEW_DOUBLE_LINE_SYMBOL + '\n')
    lines = text.split('\n')
    i = 0
    results = []

    for line in lines:
        front_side, back_side = quiz_on_nth_line(i, lines)
        results.append((front_side, back_side))
        i += 1
    return results


def quiz_on_nth_line(n: int, lines: List[str], long_version=False) -> Tuple[str, str]:
    i = 0
    front_side = ''
    back_side = ''
    for line in lines:
        if i == n - 1:
            front_side += line + '\n'
        elif i == n:
            front_side += str(i + 1) + ') ' + LINE_FOCUS_BLANK
            back_side = line
        elif long_version:
            front_side += LINE_NON_FOCUS_BLANK + '\n'
        i += 1
    front_side = front_side.replace(NEW_DOUBLE_LINE_SYMBOL, '\n')
    back_side = back_side.replace(NEW_DOUBLE_LINE_SYMBOL, '\n')
    return front_side, back_side
