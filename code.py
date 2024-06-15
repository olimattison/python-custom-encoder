# Encoding / Decoding functions

def encode(input_path, output_path, key):
    with open(input_path, "r") as i:
        raw_file = i.read()
    encoded_string = ""
    for char in raw_file:
        if char in key:
            encoded_string += key[char]
        else:
            encoded_string += char
    with open(output_path, "w") as o:
        o.write(encoded_string)


def encode_text(input_text, key):
    encoded_string = ""
    for char in input_text:
        if char in key:
            encoded_string += key[char]
        else:
            encoded_string += char
    return encoded_string


def decode(encoded_file, output_path, key):
    with open(encoded_file, 'r') as e:
        encoded_input = e.read()
    decoded_string = ""
    i = 0
    while i < len(encoded_input):
        found = False
        for k, v in key.items():
            if encoded_input[i:i + len(v)] == v:
                decoded_string += k
                i += len(v)
                found = True
                break
        if not found:
            decoded_string += encoded_input[i]
            i += 1
    with open(output_path, 'w') as o:
        o.write(decoded_string)


def decode_text(encoded_text, key):
    decoded_string = ""
    i = 0
    while i < len(encoded_text):
        found = False
        for k, v in key.items():
            if encoded_text[i:i + len(v)] == v:
                decoded_string += k
                i += len(v)
                found = True
                break
        if not found:
            decoded_string += encoded_text[i]
            i += 1

    return decoded_string


