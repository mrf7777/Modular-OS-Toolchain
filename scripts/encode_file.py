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
    print("    python.exe encode_file.py <e|d> <source file> <destination file>")
    print("Description:")
    print("    If \"source file\" exists, it is assumed to be a raw text file. Its contents are encoded")
    print("        into \"Modular OS\" encoding. A file must be in \"Modular OS\" encoding before it can")
    print("        be uploaded into a Scratch 3.0 list correctly.")
    print("")
    print("    In the <e|d> field, substitute an 'e' to encode the source into Modular OS encoding.")
    print("    Substitute a 'd' to decode the source into raw text from Modular OS encoding.")
    print("")
    print("    The encoded contents are written to \"destination file\". The file is created or cleared first.")


def encode_string(string):
    encoded_string = string.replace("\\", "\\\\")  # replace backslash with double backslash
    encoded_string = encoded_string.replace("\"", "\\q")  # replace quotes with backslash q
    encoded_string = encoded_string.replace(",", "\\c")  # replace comma with backslash comma
    return encoded_string


# decoding can be tricky using replace. Therefore, a custom loop is used.
def decode_string(string):
    decoded_string = ""
    previous_char = None
    for char in string:
        if previous_char == '\\':
            if char == '\\':
                decoded_string += '\\'
            elif char == 'q':
                decoded_string += '"'
            elif char == 'c':
                decoded_string += ','
            else:
                decoded_string += char
            previous_char = None    # in case the current char is a backslash, this ensures correct decoding of
            # backslashes
        elif char == '\\':
            previous_char = char
        else:
            decoded_string += char
            previous_char = char

    return decoded_string

def encode_file(src_file, targ_file):
    for line in src_file:
        targ_file.write(encode_string(line))


def decode_file(src_file, targ_file):
    for line in src_file:
        targ_file.write(decode_string(line))


def main(args):
    # guards

    # ensure that there are a correct number of arguments
    if len(args) != 4:
        print_usage_message()
        sys.exit(0)

    # give names to the arguments
    encode_or_decode = args[1]
    source_filename = args[2]
    destination_filename = args[3]

    # ensure that the client has selected to encode or decode
    if encode_or_decode not in ["e", "d"]:
        print_usage_message()
        sys.exit(0)

    # now it is time to attempt to open files
    source_file = None
    try:
        source_file = open(source_filename, "rt")
    except OSError:
        print("File", source_filename, "does not exist or could not be opened.")
        sys.exit(1)

    destination_file = None
    try:
        destination_file = open(destination_filename, "wt")
    except OSError:
        print("File", destination_filename, "could not be cleared, be created, or does not exist.")
        sys.exit(1)

    # files opened, do the encoding or decoding
    if encode_or_decode == "e":
        encode_file(source_file, destination_file)
    elif encode_or_decode == "d":
        decode_file(source_file, destination_file)
    else:
        print("Fatal error. Encode or decode option not correct.")
        sys.exit(1)

    # close files
    source_file.close()
    destination_file.close()


if __name__ == "__main__":
    main(sys.argv)
