from typing import List, Tuple

from card_separation_tokens import FRONT_BACK_SEPARATOR, BETWEEN_CARD_SEPARATOR

NEW_DOUBLE_LINE_SYMBOL = '%NEW_DOUBLE_LINE%'


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
