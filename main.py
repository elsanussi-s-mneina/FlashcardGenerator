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

from line_by_line import convert_single_line_text_to_line_by_line_flashcards
from word_by_word import convert_single_line_text_to_word_by_word_flashcards


def demo_word_by_word():
    convert_single_line_text_to_word_by_word_flashcards("""This is an example sentence,
in a three line paragraph.
It is nice outside today.
""")


def demo_line_by_line():
    convert_single_line_text_to_line_by_line_flashcards("""This is an example sentence,
in a three line paragraph.
It is nice outside today.
""")
