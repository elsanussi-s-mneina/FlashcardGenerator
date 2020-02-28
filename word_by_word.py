from typing import List, Tuple

from card_separation_tokens import convert_flashcards_to_csv_text

FOCUS_BLANK = '_?_'
NON_FOCUS_BLANK = '___'
NEW_LINE_SYMBOL = ' %NEW_LINE% '


class WordByWord:
    def __init__(self):
        self.show_all_previous_words = True

    def print_text_to_word_by_word_flashcards_csv(self, text: str):
        csv_text = self.convert_text_to_flashcards_as_csv(text)
        print(csv_text)

    def convert_text_to_flashcards_as_csv(self, text: str) -> str:
        flashcards = self.convert_text_to_word_by_word_flashcards(text)
        csv_text = convert_flashcards_to_csv_text(flashcards)
        return csv_text

    def convert_text_to_word_by_word_flashcards(self, text: str) -> List[Tuple[str, str]]:
        text = text.replace('\n', NEW_LINE_SYMBOL)
        words = text.split()
        i = 0
        results = []
        for word in words:
            if not word == NEW_LINE_SYMBOL.strip():
                front_side, back_side = self.quiz_on_nth_word(i, words)
                results.append((front_side, back_side))
            i += 1
        return results

    def quiz_on_nth_word(self, n: int, words: List[str]) -> Tuple[str, str]:
        i = 0
        front_side = ''
        back_side = ''
        for word in words:
            if self.is_new_line_symbol(word):
                front_side += '\n'
            elif self.ought_to_show_word(i, n, words):
                front_side += word + ' '
            elif i == n:
                front_side += FOCUS_BLANK + self.punctuation_at_end_of_word(word) + ' '
                back_side = self.strip_punctuation_on_end(word)
            else:
                front_side += NON_FOCUS_BLANK + self.punctuation_at_end_of_word(word) + ' '
            i += 1
        return front_side, back_side

    def ought_to_show_word(self, word_index: int, target_word_index: int, words: List[str]) -> bool:
        """Determine whether a word should be spelled out fully on the front side of a card (instead of being
        covered by some sort of blank, or omitted.
        :param word_index: the index to the word we are asking the question about.
        :param target_word_index: the index to the word that the flashcard is quizzing the student on.
        :param words: the list of words
        :return: True if the word should appear as-is on the front side of the flashcard.
        """
        return word_index == target_word_index - 1 \
            or (word_index == target_word_index - 2 and self.is_new_line_symbol(words[word_index + 1]))\
            or (self.show_all_previous_words and word_index < target_word_index)

    @staticmethod
    def punctuation_at_end_of_word(word: str) -> str:
        if word.endswith('.') or word.endswith(',') or word.endswith('!') or word.endswith('?'):
            return word[-1]
        else:
            return ''

    @staticmethod
    def strip_punctuation_on_end(word: str) -> str:
        if word.endswith('.') or word.endswith(',') or word.endswith('!') or word.endswith('?'):
            return word[:-1]
        else:
            return word

    @staticmethod
    def is_new_line_symbol(token: str) -> bool:
        return token == NEW_LINE_SYMBOL.strip()

    def configure_to_show_only_one_previous_word_on_front_side(self):
        self.show_all_previous_words = False

    def configure_to_show_all_previous_words_on_front_side(self):
        self.show_all_previous_words = True
