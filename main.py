import code

# CUSTOMIZE KEY FOR CUSTOM ENCODING
key = {
    '.': '0-0',
    '!': '-0-',
    ' ': '0*1',
    'a': '%1-',
    'A': '0--',
    'e': '00',
    'E': '10',
    'f': '0D',
    'F': 'yS'
    # 'char': 'unique_value',


}


def main():
    print("Select Mode")
    input_type = input("File input mode: 1 \nor\nText Input Mode: 2 \n(1 or 2): ")
    mode = input("encode message: 1  \ndecode message: 2\n(1 or 2): ")

    if input_type == "1":
        print("File Input Mode selected")
        if mode == "1":
            print("encoding mode selected")
            unencoded_path = input("unencoded txt file path: ")
            encoded_path = input("output path: ")
            try:
                print(code.encode(unencoded_path, encoded_path, key))
            except BaseException as e:
                print(f"an error occurred: {e}")

        if mode == "2":
            print("decoding mode selected")
            encoded_path = input("encoded txt file path: ")
            decoded_path = input("output file path: ")
            try:
                code.decode(encoded_path, decoded_path, key)
            except BaseException as e:
                print(f"an error occurred: {e}")

            if mode != "1" and mode != "2":
                print("invalid input! select '1' or '2'")

    # TEXT INPUT MODE
    elif input_type == "2":
        print("Text Input Mode selected")
        if mode == "1":
            unencoded_text = input("Enter unencoded text: ")
            print("encoding mode selected")
            try:
                output = code.encode_text(unencoded_text, key)
                print(output)
            except BaseException as e:
                print(f"an error occurred: {e}")

        if mode == "2":
            encoded_text = input("Enter encoded text: ")
            print("decoding mode selected")
            try:
                output = code.decode_text(encoded_text, key)
                print(output)
            except BaseException as e:
                print(f"an error occurred: {e}")

            if mode != "1" and mode != "2":
                print("invalid input! select '1' or '2'")


if __name__ == '__main__':
    main()
