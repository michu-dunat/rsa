import library

if __name__ == '__main__':
    text, file_name = library.get_text()
    public_key = library.get_key()

    encrypted_char_list = []
    for char in text:
        char_unicode = ord(char)
        encrypted_char = pow(char_unicode, public_key[1]) % public_key[0]
        encrypted_char_list.append(encrypted_char)

    f = open("encrypted-" + file_name, "w")
    f.write(str(encrypted_char_list))
    f.close()
