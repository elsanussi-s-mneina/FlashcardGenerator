import unittest

from word_by_word import is_new_line_symbol, strip_punctuation_on_end, convert_text_to_flashcards_as_csv


class TestWordByWord(unittest.TestCase):
    def test_is_new_line_symbol(self):
        self.assertTrue(is_new_line_symbol('%NEW_LINE%'))

    def test_strip_punctuation_on_end__comma(self):
        result = strip_punctuation_on_end('thing,')
        self.assertEqual(result, 'thing')

    def test_strip_punctuation_on_end__period(self):
        result = strip_punctuation_on_end('think.')
        self.assertEqual(result, 'think')

    def test_strip_punctuation_on_end__question_mark(self):
        result = strip_punctuation_on_end('thank?')
        self.assertEqual(result, 'thank')

    def test_convert_flashcards_to_csv_text__one_words(self):
        result = convert_text_to_flashcards_as_csv('fox')
        expected = '_?_ $%$%fox*&*&'
        self.assertEqual(expected, result)

    def test_convert_flashcards_to_csv_text__two_words(self):
        result = convert_text_to_flashcards_as_csv('The quick')
        expected = '_?_ ___ $%$%The*&*&The _?_ $%$%quick*&*&'
        self.assertEqual(expected, result)

    def test_convert_flashcards_to_csv_text__three_words(self):
        result = convert_text_to_flashcards_as_csv('The quick brown')
        expected = '_?_ ___ ___ $%$%The*&*&The _?_ ___ $%$%quick*&*&___ quick _?_ $%$%brown*&*&'
        self.assertEqual(expected, result)
