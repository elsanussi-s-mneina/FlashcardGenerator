from line_by_line import LineByLine
from word_by_word import WordByWord
from input_text import read_text_from_file
from output_text import write_text_to_line_by_line_export_file, write_text_to_word_by_word_export_file


def read_text_convert_to_flashcards_and_write_results(input_file_path: str, input_file_name: str, language: str):
    input_text = read_text_from_file(input_file_path + input_file_name)
    line_by_line_generator = LineByLine()
    line_by_line_generator.configure_to_replace_lines_with_as_many_blanks_as_words()
    output_csv_text_line_by_line = line_by_line_generator.convert_text_to_flashcards_as_csv(input_text)
    write_text_to_line_by_line_export_file(input_file_name, language, output_csv_text_line_by_line)
    word_by_word_generator = WordByWord()
    output_csv_text_word_by_word = word_by_word_generator.convert_text_to_flashcards_as_csv(input_text)
    write_text_to_word_by_word_export_file(input_file_name, language, output_csv_text_word_by_word)
