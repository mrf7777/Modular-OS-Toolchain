import sys
import os
import re


def print_usage_message():
    print("")
    print("Usage:")
    print("python.exe format_code.py <source code file> <destination file>")
    print("")
    print("This formats the contents of \"source code file\", written to \"destination file\",")
    print("    and fixes it to work with Modular OS.")
    print("")
    print("If the destination file exists, it is cleared and overwritten.")
    print("If the destination file does not exists, the file is created and written.")


"""
Pass an open file ready for reading text.
Returns a python list of strings which are tokens.
Tokens include individual literal expressions and commands.
"""


def get_tokens(file):
    lines = file.readlines()  # get all of the lines from the file

    # assume no token can be split between two lines.
    tokens = []
    for line in lines:
        toks_from_line = get_tokens_from_line(line)
        for tok in toks_from_line:
            tokens.append(tok)
    return tokens


# given a line, get the tokens from it
def get_tokens_from_line(line):
    # remove trailing whitespace
    trimmed_line = line.strip()  # remove trailing whitespace

    # remove comments from the line if there are any
    fixed_line = remove_comments(trimmed_line)

    # regex reference: "\".*?\"|[\w:]+"gm
    #   identifies individual literals or commands, does not support escape chars

    token_pattern = re.compile(r"/\".*?\"|[\w:]+/gm")
    tokens = re.findall(token_pattern, fixed_line)
    return tokens


# given a line, it removes comments from the code.
# comments start with a # character and continue until the end of the line
def remove_comments(line):
    # search for a comment starter
    index_of_comment_start = line.find("#")
    # if there was no comment starter found
    if index_of_comment_start == -1:
        # return the whole line
        return line
    # if a comment was found
    else:
        # return the part that is not commented out
        return line[0:index_of_comment_start]


# given a file handle open for writing text, write the list of tokens to it
def write_tokens_to_file(file, tokens):
    # exit function if there are no tokens
    if len(tokens) == 0:
        return

    # keep a counter
    counter = 0
    # add token to output file on each line
    for token in tokens:
        file.write(token)
        # only create a new line if there is another token
        # do not create a new line on the last token
        if counter < len(tokens) - 1:
            file.write("\n")
        counter += 1
    return file


def main(args):
    # guards. Fail program immediately if input is invalid

    # test for correct amount of inputs
    if len(args) != 3:
        print_usage_message()
        sys.exit(0)

    # test to see if input file exists.
    source_filename = args[1]
    if not os.path.exists(source_filename):
        print("File ", source_filename, " does not exists or is inaccessible.")
        sys.exit(1)  # failure

    # attempt to open file
    source_file_handle = None
    try:
        source_file_handle = open(source_filename, "rt")  # open source file for reading text
    except OSError:
        print("File ", source_filename, " could not be opened.")
        sys.exit(1)

    # if the file for some reason is still not opened, exit now.
    if source_file_handle is None:
        print("File ", source_filename, " could not be opened.")
        sys.exit(1)

    # file opened, now do processing.
    tokens = get_tokens(source_file_handle)

    # tokens are gotten, close the source file
    source_file_handle.close()

    # now write tokens to output file
    # attempt to open output file
    destination_filename = args[2]

    destination_file_handle = None
    try:
        destination_file_handle = open(destination_filename, "wt")
    except OSError:
        print("File ", destination_filename, " could not be written to or created.")
        sys.exit(1)

    # if for some reason the output file is not open, exit now.
    if destination_file_handle is None:
        print("File ", destination_filename, " could not be written to or created.")
        sys.exit(1)

    # output file opened, now write to it
    write_tokens_to_file(destination_file_handle, tokens)

    # close the output file
    destination_file_handle.close()


if __name__ == "__main__":
    main(sys.argv)
