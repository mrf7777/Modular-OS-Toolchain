import sys

"""
"Modular OS" encoding is an invertible transformation on text.
It is defined as the following executed in this order:
    -all occurrences of backslash are replaced with a double backslash
    -all occurrences of " are replaced with a backslash quote
    -all occurrences of , are replaced with a backslash comma

To undo to transformation, undo each of the steps in reverse order.

This encoding ensures that text files can be uploaded to a Scratch 3.0 list.
Commas and quote characters provide unexpected behavior upon importing.
"""


def encode_string(string):
    encoded_string = string.replace("\\", "\\\\")  # replace backslash with double backslash
    encoded_string = encoded_string.replace("\"", "\\q")  # replace quotes with backslash q
    encoded_string = encoded_string.replace(",", "\\c")  # replace comma with backslash comma
    return encoded_string


def decode_string(string):
    decoded_string = string.replace("\\c", ",")
    decoded_string = decoded_string.replace("\\q", "\"")
    decoded_string = decoded_string.replace("\\\\", "\\")
    return decoded_string


def encode_file(src_file, targ_file):
    for line in src_file:
        targ_file.write(encode_string(line))


def decode_file(src_file, targ_file):
    for line in src_file:
        targ_file.write(encode_string(line))


def main(args):
    pass


if __name__ == "__main__":
    main(sys.argv)
