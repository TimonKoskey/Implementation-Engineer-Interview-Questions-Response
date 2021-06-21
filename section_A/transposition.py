def split(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, text):
    order = {
      int(val): num for num, val in enumerate(key)
    }
    ciphertext = ''

    for index in sorted(order.keys()):
        for part in split(text, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext