import os


def write_text_to_line_by_line_export_file(file_name: str, language: str, contents: str) -> None:
    _write_text_to_export_file(file_name, language, contents, 'Line by Line')


def write_text_to_word_by_word_export_file(file_name: str, language: str, contents: str) -> None:
    _write_text_to_export_file(file_name, language, contents, 'Word by Word')


def _write_text_to_export_file(file_name: str, language: str, contents: str, strategy: str) -> None:
    make_missing_path('output_data')
    make_missing_paths_for_language(language, strategy)
    with open('output_data/' + language + '/' + strategy + '/' + file_name, 'w') as file:
        file.write(contents)


def make_missing_paths_for_language(language, strategy):
    make_missing_path('output_data/' + language + '/' + strategy)


def make_missing_path(new_path):
    # from https://stackoverflow.com/questions/1274405/how-to-create-new-folder
    if not os.path.exists(new_path):
        os.makedirs(new_path)
