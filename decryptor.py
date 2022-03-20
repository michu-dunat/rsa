import library

if __name__ == '__main__':
    encrypted_text, file_name = library.get_text()
    private_key = library.get_key()

    encrypted_unicode_as_string_list = encrypted_text.split(',')
    encrypted_unicode_as_string_list[0] = encrypted_unicode_as_string_list[0].removeprefix('[')
    encrypted_unicode_as_string_list[len(encrypted_unicode_as_string_list) - 1] = encrypted_unicode_as_string_list[len(encrypted_unicode_as_string_list) - 1].removesuffix(']')
    encrypted_unicode_list = [int(x) for x in encrypted_unicode_as_string_list]

    decrypted_text = ""
    for unicode_char in encrypted_unicode_list:
        decrypted_unicode = (int(unicode_char) ** private_key[1]) % private_key[0]
        char = chr(decrypted_unicode)
        decrypted_text += char

    correct_file_name = file_name

    if file_name.startswith('encrypted-'):
        correct_file_name = file_name.removeprefix('encrypted-')

    f = open("decrypted-" + correct_file_name, "w")
    f.write(str(decrypted_text))
    f.close()
