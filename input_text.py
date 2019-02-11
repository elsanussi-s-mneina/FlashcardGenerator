def read_text_from_file(file_name):
    file = open('input_data/' + file_name, 'r')
    lines = file.readlines()
    return str().join(lines)