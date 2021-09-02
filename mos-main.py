import sys
import os
import scripts.format_code
import scripts.encode_file

def print_default_usage_message():
    print("")
    print("Usage:")
    print("    python.exe mos-main.py <command> <options>")
    print("Commands (substitute <command>):")
    print("    compile")
    print("    encode")
    print("    help")
    print("Description:")
    print("    This is a multi-tool that allows users to do anything related to Modular OS.")
    print("    For how to use a specific command, type \"python.exe mos-main.py help <command>\".")


def print_usage_message(command=None):
    if command is None:  # when no command is passed, the default message.
        print_default_usage_message()
    elif command == "compile":
        print("")
        print("Usage:")
        print("    python.exe mos-main.py compile <source file> <target file> <options>")
        print("Description:")
        print("    Given a Modular OS source code file named <source file>, the code is compiled,")
        print("        formatted, and encoded.")
        print("    The result is written to a file named <target file>. If the file exists, it is")
        print("        first cleared. If not, it is created.")
        print("Options:")
        print("    -n      The output will not be encoded into Modular OS, contrary to default behavior.")
    elif command == "encode":
        print("")
        print("Usage:")
        print("    python.exe mos-main.py encode <source file> <target file> <options>")
        print("Description:")
        print("    Given a text file named <source file>, it is either encoded or decoded into or from")
        print("        Modular OS encoding; the exact behavior depends on the options field. An option")
        print("        is required to work.")
        print("    The result is written to a file named <target file>. If the file exists, it is")
        print("        first cleared. If not, it is created.")
        print("Options:")
        print("    -e      Encode the text from the source and write it to the target file")
        print("    -d      Decode the text from the source and write it to the target file")
    elif command == "help":
        print("")
        print("Usage:")
        print("    python.exe mos-main.py help <command or subject>")
        print("Description:")
        print("    Given a following command or subject term, the help message is displayed.")
    else:
        print_default_usage_message()


def main(args):
    pass


if __name__ == "__main__":
    main(sys.argv)
