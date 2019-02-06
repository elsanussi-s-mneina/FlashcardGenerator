from typing import List, Tuple

FRONT_BACK_SEPARATOR = '$%$%'
BETWEEN_CARD_SEPARATOR = '*&*&'


def convert_flashcards_to_csv_text(flashcards: List[Tuple[str, str]]) -> str:
    csv_text = ''
    for (front_side, back_side) in flashcards:
        csv_text += front_side
        csv_text += FRONT_BACK_SEPARATOR
        csv_text += back_side
        csv_text += BETWEEN_CARD_SEPARATOR
    return csv_text
