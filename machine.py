from instraction import morse_instruction


def convert_to(entry):
    char_list = []
    word_list = entry.split()
    for word in word_list:
        char_list.extend([char.upper() for char in word])
        char_list.append(' ')

    code_list = [morse_instruction[char] for char in char_list]

    code = ''
    for char in code_list:
        code += char
    return code
