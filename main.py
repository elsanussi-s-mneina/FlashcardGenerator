"""
Let me create a program that takes text
like "The quick brown fox jumped over the lazy dog" (representing a text that a person wants to memorize verbatim),
and returns a list of tuples (representing flashcards)
like the following:

Front: The ___
Back: quick

Front: quick ___
Back: brown

and so on.


options:
  length of underscore for replacing a word
  whether the underscore is fixed in length, or is exactly the same length as the word
  clue_length: number of words, or characters on the front of the card before the blank
  clue_type: whether the clue is in words, or characters
"""
import os

from line_by_line import convert_text_to_line_by_line_flashcards
from word_by_word import WordByWord
from batch_operations import read_text_convert_to_flashcards_and_write_results


DEMO_INPUT_TEXT = """This is an example sentence,
in a three line paragraph.
It is nice outside today.
"""


def demo_word_by_word():
    print('Demonstrating converting text into word-by-word flashcards.')
    report_demo_text()
    print('Output:')
    word_by_word_generator = WordByWord()
    word_by_word_generator.print_text_to_word_by_word_flashcards_csv(DEMO_INPUT_TEXT)
    print('\n\n')


def demo_line_by_line():
    print('Demonstrating converting text into line-by-line flashcards.')
    report_demo_text()
    print('Output:')
    convert_text_to_line_by_line_flashcards(DEMO_INPUT_TEXT)
    print('\n\n')


def report_demo_text():
    print('The text to be converted is:')
    print(DEMO_INPUT_TEXT)
    print()


def demo():
    demo_word_by_word()
    demo_line_by_line()


def main():
    print('reading all texts for memorization from directory: input_data')
    languages = os.listdir('input_data')
    for language in languages:
        memorization_text_filenames = os.listdir('input_data/' + language)
        for input_text_filename in memorization_text_filenames:
            read_text_convert_to_flashcards_and_write_results(language + '/', input_text_filename, language)
    print('Look in the directory at output_data for CSV files that you can export')
    print('These files contain the generated flashcards.')
    print('Program terminated normally.')


if __name__ == '__main__':
    main()