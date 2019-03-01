import unittest

from word_by_word import WordByWord

#    is_new_line_symbol, strip_punctuation_on_end, convert_text_to_flashcards_as_csv, \
#    quiz_on_nth_word, quiz_on_nth_word_show_all_previous_words


class TestWordByWord(unittest.TestCase):
    def test_is_new_line_symbol(self):
        self.assertTrue(WordByWord.is_new_line_symbol('%NEW_LINE%'))

    def test_strip_punctuation_on_end__comma(self):
        result = WordByWord.strip_punctuation_on_end('thing,')
        self.assertEqual(result, 'thing')

    def test_strip_punctuation_on_end__period(self):
        result = WordByWord.strip_punctuation_on_end('think.')
        self.assertEqual(result, 'think')

    def test_strip_punctuation_on_end__question_mark(self):
        result = WordByWord.strip_punctuation_on_end('thank?')
        self.assertEqual(result, 'thank')

    def test_convert_flashcards_to_csv_text__one_words(self):
        generator = WordByWord()
        result = generator.convert_text_to_flashcards_as_csv('fox')
        expected = '_?_ $%$%fox*&*&'
        self.assertEqual(expected, result)

    def test_convert_flashcards_to_csv_text__two_words(self):
        generator = WordByWord()
        result = generator.convert_text_to_flashcards_as_csv('The quick')
        expected = '_?_ ___ $%$%The*&*&The _?_ $%$%quick*&*&'
        self.assertEqual(expected, result)

    def test_convert_flashcards_to_csv_text__three_words(self):
        generator = WordByWord()
        generator.configure_to_show_only_one_previous_word_on_front_side()
        result = generator.convert_text_to_flashcards_as_csv('The quick brown')
        expected = '_?_ ___ ___ $%$%The*&*&The _?_ ___ $%$%quick*&*&___ quick _?_ $%$%brown*&*&'
        self.assertEqual(expected, result)

    def test_quiz_on_nth_word__first_word(self):
        generator = WordByWord()
        result = generator.quiz_on_nth_word(0, ['first', 'second', 'third', 'fourth'])
        expected = ('_?_ ___ ___ ___ ', 'first')
        self.assertEqual(expected, result)

    def test_quiz_on_nth_word__second_word(self):
        generator = WordByWord()
        result = generator.quiz_on_nth_word(1, ['first', 'second', 'third', 'fourth'])
        expected = ('first _?_ ___ ___ ', 'second')
        self.assertEqual(expected, result)

    def test_quiz_on_nth_word__fourth_word(self):
        generator = WordByWord()
        generator.configure_to_show_only_one_previous_word_on_front_side()
        result = generator.quiz_on_nth_word(3, ['first', 'second', 'third', 'fourth'])
        expected = ('___ ___ third _?_ ', 'fourth')
        self.assertEqual(expected, result)

    def test_quiz_on_nth_word__fourth_word_again(self):
        generator = WordByWord()
        generator.configure_to_show_only_one_previous_word_on_front_side()
        result = generator.quiz_on_nth_word(3, ['apple', 'banana', 'orange', 'pear'])
        expected = ('___ ___ orange _?_ ', 'pear')
        self.assertEqual(expected, result)

    def test_quiz_on_nth_word_show_all_previous_words__fourth_word_again(self):
        generator = WordByWord()
        generator.configure_to_show_all_previous_words_on_front_side()
        result = generator.quiz_on_nth_word(3, ['apple', 'banana', 'orange', 'pear'])
        expected = ('apple banana orange _?_ ', 'pear')
        self.assertEqual(expected, result)
