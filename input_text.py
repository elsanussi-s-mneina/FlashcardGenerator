def read_text_from_file(file_name: str) -> str:
    with open('input_data/' + file_name, 'r') as file:
        lines = file.readlines()
        return str().join(lines)
