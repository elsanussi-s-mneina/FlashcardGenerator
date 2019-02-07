import unittest

from line_by_line import convert_text_to_flashcards_as_csv, quiz_on_nth_line, \
    custom_blank_line_with_spaces_between_words_shown


class TestLineByLine(unittest.TestCase):
    def test_convert_flashcards_to_csv_text__one_words(self):
        result = convert_text_to_flashcards_as_csv('fox\ndove', blind_blank=True)
        expected = '1) _____?_____$%$%fox*&*&fox\n2) _____?_____$%$%dove*&*&'
        self.assertEqual(expected, result)

    def test_convert_flashcards_to_csv_text__one_words__blanks_with_spaces(self):
        result = convert_text_to_flashcards_as_csv('fox\ndove', blind_blank=False)
        expected = '1) ___$%$%fox*&*&fox\n2) ____$%$%dove*&*&'
        self.assertEqual(expected, result)

    def test_quiz_on_nth_line___first_line(self):
        result = quiz_on_nth_line(0, ['line1word1 line1word2', 'line2word1', 'line3word1'])
        expected = ('1) _____?_____', 'line1word1 line1word2')
        self.assertEqual(expected, result)

    def test_quiz_on_nth_line___not_first_line(self):
        result = quiz_on_nth_line(1, ['line1word1 line1word2', 'line2word1', 'line3word1'])
        expected = ('line1word1 line1word2\n2) _____?_____', 'line2word1')
        self.assertEqual(expected, result)

    def test_custom_blank_line_with_spaces_between_words_shown(self):
        result = custom_blank_line_with_spaces_between_words_shown('first second third')
        expected = '_____ ______ _____'
        self.assertEqual(expected, result)

    def test_custom_blank_line_with_spaces_between_words_shown__with_punctuation(self):
        result = custom_blank_line_with_spaces_between_words_shown('first, second; third.')
        expected = '_____, ______; _____.'
        self.assertEqual(expected, result)

    def test_custom_blank_line_with_spaces_between_words_shown__with_numerals(self):
        result = custom_blank_line_with_spaces_between_words_shown('1, 2; third.')
        expected = '_, _; _____.'
        self.assertEqual(expected, result)

    def test_quiz_on_nth_line___first_line__blanks_with_spaces(self):
        result = quiz_on_nth_line(0, ['line1word1 line1word2', 'line2word1', 'line3word1'],
                                  blind_blank=False)
        expected = ('1) __________ __________', 'line1word1 line1word2')
        self.assertEqual(expected, result)

    def test_quiz_on_nth_line___not_first_line__blanks_with_spaces(self):
        result = quiz_on_nth_line(1, ['line1word1 line1word2', 'line2word1', 'line3word1'],
                                  blind_blank=False)
        expected = ('line1word1 line1word2\n2) __________', 'line2word1')
        self.assertEqual(expected, result)
