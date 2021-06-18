def ceaser_cipher_encrypt(text,pattern):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + pattern - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + pattern - 97) % 26 + 97)

        else:
            result += chr((ord(char) + pattern - 33) % 14 + 33)

    return result