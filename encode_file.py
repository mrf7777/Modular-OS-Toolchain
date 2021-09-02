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

def print_usage_message():
    print("")
    print("Usage:")
    print("    python.exe encode_file.py <source file> <destination file>")
    print("Description:")
    print("    If \"source file\" exists, it is assumed to be a raw text file. Its contents are encoded")
    print("        into \"Modular OS\" encoding. A file must be in \"Modular OS\" encoding before it can")
    print("        be uploaded into a Scratch 3.0 list correctly.")
    print("")
    print("    The encoded contents are written to \"destination file\". The file is created or cleared first.")


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
    if len(args) != 3:
        print_usage_message()
        sys.exit(0)


if __name__ == "__main__":
    main(sys.argv)
