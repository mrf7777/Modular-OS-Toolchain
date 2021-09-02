import sys
import os
import tempfile

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
    # guards

    # this should never happen
    if len(args) == 0:
        print("Fatal Error. There are no arguments.")
        sys.exit(1)

    # when no arguments are passed
    if len(args) == 1:
        print_usage_message(None)
        sys.exit(0)

    # there are at least 2 arguments / 1 passed argument

    command = args[1]   # capture the first passed argument

    if command == "help":

        # if no command or subject. or if too many commands or subjects
        if len(args) <= 2 or len(args > 3):
            print_usage_message("help")
            sys.exit(0)

        # there should be exactly 2 passed arguments: help <command or subject>
        print_usage_message(args[2])

    if command == "compile":

        # ensure there are a correct number of arguments
        if len(args) < 3 or len(args) > 4:
            print_usage_message("compile")
            sys.exit(0)

        # there should now be between 2 to 3 passed arguments

        # see if the user wants the compiled code to be encoded into Modular OS encoding
        # by default, yes.
        encode_output = True
        if len(args) == 4:  # ensure that they actually made an option.
            if args[3] == "-n":
                encode_output = False
            else:
                print("Compile option \"" + args[3] + "\" is not valid.")
                print_usage_message("compile")
                sys.exit(0)

        # arguments processed and options interpreted. call proper script

        # take this route if encoding is to be done after
        if encode_output:
            temp_file, temp_filename = tempfile.mkstemp(text=True)
            scripts.format_code.main(["dummy", args[1], temp_filename])
            scripts.encode_file.main(["dummy", temp_filename, args[2]])
            os.close(temp_file)
        # take this route if no encoding is to be done
        else:
            scripts.format_code.main(["dummy", args[1], args[2]])

    if command == "encode":

        # ensure that are a correct number of arguments
        if len(args) != 4:
            print_usage_message("encode")
            sys.exit(0)

        # label the arguments
        source_filename = args[1]
        target_filename = args[2]
        encode_option = args[3]

        # ensure the user provided a valid encode/decode option.
        if encode_option not in ["-e", "-d"]:
            print_usage_message("encode")
            sys.exit(0)

        # perform the encoding or decoding
        # encode option
        if encode_option == "-e":
            scripts.encode_file.main(["dummy", "e", source_filename, target_filename])
        elif encode_option == "-d":
            scripts.encode_file.main(["dummy", "d", source_filename, target_filename])
        else:
            print("Fatal error. Invalid encoding option.")
            sys.exit(1)






if __name__ == "__main__":
    main(sys.argv)
