def split(seq, length):
    # for i in range(0, len(seq), length):
    #     print(i)
    #     print(seq[i:i + length])
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, text):
    order = {
      int(val): num for num, val in enumerate(key)
    }
    # print(order)
    ciphertext = ''

    for index in sorted(order.keys()):
        # print(index)
        for part in split(text, len(key)):
            print(part)
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext