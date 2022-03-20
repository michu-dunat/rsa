def get_text():
    file_name = input('File name: ')
    f = open(file_name, "r")
    text = f.read()
    f.close()
    return text, file_name


def get_key():
    file_name = input('Key file name: ')
    f = open(file_name, "r")
    text = f.read()
    f.close()
    return eval(text)
