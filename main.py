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
