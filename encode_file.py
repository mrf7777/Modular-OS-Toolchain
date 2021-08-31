import sys


def encode_string(string):
    encoded_string = string.replace("\"", "\\q")    # replace quotes with backslash q
    encoded_string = encoded_string.replace("\\", "\\\\")   # replace backslash with double backslash
    encoded_string = encoded_string.replace(",", "\c")      # replace comma with backslash comma
    return encoded_string


def main(args):
    pass


if __name__ == "__main__":
    main(sys.argv)