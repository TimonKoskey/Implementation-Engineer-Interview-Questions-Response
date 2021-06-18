rot13trans = bytearray.maketrans(str.encode('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'), 
   str.encode('NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

def rot13(text):
    return text.translate(rot13trans)