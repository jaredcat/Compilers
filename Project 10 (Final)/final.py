# Pooja Srivastava & Jared Kotoff
# CS 323
# Final Project
# December 11, 2014

import sys
import re
import string


# Key
# [0, "PROGRAM", ";", "VAR", "BEGIN", "END.", ":", ",", "INTEGER", "WRITE", "(", ")", "=", "+", "-", "*", "/", "0",
# "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "$"]
TABLE = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0],
    [0, 0, 5, 0, 0, 0, 5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 0],
    [0, 0, 0, 0, 0, 0, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 11, 11, 11, 11, 0],
    [0, 0, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 12, 12, 12, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 17, 17, 17, 17, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 18, 18, 0, 0, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 0],
    [0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 19, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 22, 22, 0, 0, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 0],
    [0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 25, 25, 23, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 0, 0, 27, 27, 0, 0, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 26, 26, 26, 26, 26, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 29, 0, 0, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 0, 0, 0, 0, 0, 0],
    [0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 31, 31, 31, 31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 33, 0, 0, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 46, 47, 48, 49, 0]
]
# Arrays for looking up and conversion of input for table
COLUMNS = [0, "PROGRAM", ";", "VAR", "BEGIN", "END.", ":", ",", "INTEGER", "WRITE", "(", ")", "=", "+", "-", "*", "/",
           "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "$"]
ROWS = [0, "program", "identifier", "identifiertail", "dec-list", "dec", "dectail", "type", "stat-list",
        "stat-listtail", "stat", "write", "assign", "expr", "exprtail", "term", "termtail", "factor", "number",
        "numbertail", "sign", "digit", "id"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
LETTERS = ["a", "b", "c", "d", "e"]
SYMBOLS = [",", ";", ":", "(", ")", "-", "+", "-", "*", "/", "=", "."]
RESERVED_WORDS = ["PROGRAM", "VAR", "BEGIN", "END.", "INTEGER", "WRITE"]

# The predictive set that the numbers from the table above correspond to
PREDICTIVE_SET = [0, ["PROGRAM", "identifier", ";", "VAR", "dec-list", "BEGIN", "stat-list", "END."],
                  ["id", "identifiertail"], ["id", "identifiertail"], ["digit", "identifiertail"], ["%"],
                  ["dec", ":", "type", ";"], ["identifier", "dectail"], [",", "dec"], ["%"], ["INTEGER"],
                  ["stat", "stat-listtail"], ["stat-list"], ["%"], ["write"], ["assign"],
                  ["WRITE", "(", "identifier", ")", ";"], ["identifier", "=", "expr", ";"], ["term", "exprtail"],
                  ["+", "expr"], ["-", "expr"], ["%"], ["factor", "termtail"], ["*", "factor", "termtail"],
                  ["/", "factor", "termtail"], ["%"], ["identifier"], ["number"], ["(", "expr", ")"],
                  ["sign", "digit", "numbertail"], ["digit", "numbertail"], ["%"], ["+"], ["-"], ["%"], ["0"], ["1"],
                  ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["a"], ["b"], ["c"], ["d"], ["e"]]


# This function reads a file and parses it into a more standardized format
def read_file(infile, outfile):
    # Opens the output file
    with open(outfile, "w") as g:
        # Loop over each line in the file
        with open(infile, "r") as f:
            for line in f:

                comment = " *)"
                sem = ";"

                if not line.startswith("\n"):

                    # Strip the line to remove whitespace.
                    line = line.strip('\t\r')
                    line = line.replace("=", " = ")
                    line = line.replace("+", " + ")
                    line = line.replace("<<", " << ")
                    line = line.replace(";", " ;")
                    line = line.replace(",", " ,")
                    line = line.replace(")", " )")
                    line = line.replace("* )", "*)")
                    line = line.replace("(", " (")
                    line = line.replace("\t", " ")

                    if comment in line:
                        if sem not in line:
                            line = line.replace(line, "")

                        else:
                            line = line.replace(sem, ";\n")

                    if line.startswith('\n'):
                        g.write("")

                    t_list = line.split(" " or ";")

                    for token in t_list:
                        if token.startswith("(*"):
                            g.write("")
                            break

                        if not token == '':

                            if not token.endswith('\n'):
                                g.write(token + " ")
                            else:
                                g.write(token)


# This function traces the input against the grammar to see if it has any errors
def check_input(file):
    fail = 0
    read = ""
    token =""
    k = 0
    stack = ([])
    stack.append('$')
    stack.append("program")
    print_stack(stack)

    with open(file, "r") as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.split(" " or ';')
            next_line = False
            i = 0
            while stack:
                if next_line:
                    break
                # Looks at the last item in the stack
                token = stack.pop()
                print_stack(stack)
                # First item in the input
                read = line[i]

                # If at the bottom of stack and there's nothing left in the input
                if token == "$" and not read:
                    return "No error"
                # if token is a terminal
                elif token in LETTERS or token in DIGITS or token in SYMBOLS or token in RESERVED_WORDS:
                    # if there's a match, move to next input
                    if token == read:
                        i += 1
                    # if there is a match on an identifier (a-e or 0-9)
                    elif token == read[k][0]:
                        # move to the next character in the identifier
                        k += 1
                        # if at the end of the identifier
                        if k == len(read):
                            # move to next input, reset character counter
                            i += 1
                            k = 0
                    # Checks input for spelling errors against the grammar in reserved words
                    elif token in RESERVED_WORDS or token in SYMBOLS:
                        fail = 1
                        break
                    # if at the end of the line, move to the next
                    if i == len(line):
                            next_line = True
                # If token is non-terminal
                else:
                    # check if input is part of an identifier
                    if read[k][0] in LETTERS or read[k][0] in DIGITS:
                        column = COLUMNS.index(read[k][0])
                    else:
                        if read in COLUMNS:
                            column = COLUMNS.index(read)
                        else:
                            fail = 1
                            break
                    row = ROWS.index(token)
                    # look up in table and then convert using predictive set
                    parse = PREDICTIVE_SET[TABLE[row][column]]

                    # if lambda then move to next item in array
                    if parse != ['%']:
                        # if a zero is returned from table, then its not in grammar and input is rejected
                        if parse == 0:
                            fail = 1
                            break
                        # push onto stack in reverse order
                        for j in range(len(parse)-1, -1, -1):
                            stack.append(parse[j])
                        print_stack(stack)
            # If grammar was rejected for any reason
            if fail:
                if token == "program":
                    print("\n" + "PROGRAM was expected")
                    print(read + " was given")
                elif token in RESERVED_WORDS:
                    print("\n" + token + " was expected")
                    print(read + " was given")
                elif read == ")":
                    print("\n" + "( is missing")
                elif token in SYMBOLS:
                    print("\n" + token + " is missing")
                elif len(stack) > 1 and stack[len(stack)-1] in SYMBOLS:
                    print("\n" + stack[len(stack)-1] + " is missing")
                elif len(stack) > 2 and stack[len(stack)-2] in SYMBOLS:
                    print("\n" + stack[len(stack)-2] + " is missing")
                elif len(stack) > 3 and stack[len(stack)-3] in SYMBOLS:
                    print("\n" + stack[len(stack)-3] + " is missing")
                elif token == "stat-listtail":
                    print("\n" + "WRITE was expected")
                    print(read + " was given")
                elif len(stack) > 1 and stack[len(stack)-1] == "END.":
                    if read == "END":
                        print("\n" + ". is missing")
                    else:
                        print("\n" + "END. was expected")
                        print(read + " was given")
                else:
                    print("\n" + "UNKNOWN IDENTIFIER")
                return "Rejected"


# This function to print the current stack cleanly to the terminal
def print_stack(stack):
    print('Stack: ', end='')
    for i in stack:
        print(i + " ", end='')
    print()


# This function is used to print an array cleanly to terminal
# Used inside of convert_to_cpp
def print_array(array):
    print("   ", end='')
    for i in array:
        print(" " + i, end='')
    print()


# This function converts a given file into C++ code
def convert_to_cpp(file):
    print()
    print()
    with open(file, "r") as f:
        print("#include <iostream>")
        print("using name space std;")
        print("int main()")
        print("{")
        next(f)
        next(f)
        for line in f:
            line = line.strip('\n')
            line = line.split(" ")
            if "BEGIN" not in line:
                if "INTEGER" in line:
                    print("    int ", end='')
                    for i in line:
                        if i == ":":
                            print(";")
                            break
                        else:
                            print(i + " ", end='')
                elif "WRITE" in line:
                    print("    cout << ", end='')
                    for i in line:
                        if i != "WRITE" and i != "(":
                            if i != ")":
                                print(i + " << ", end='')
                            else:
                                print("endl ;")
                                break
                elif "END." in line:
                    print("    return 0 ;")
                    break
                else:
                    print_array(line)
        print("}")
    return 0


def main():
    """if len(sys.argv) != 3:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 <Python source code file> <input file> <output file>')
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2] """
    input_file = "finalv1.txt"
    output_file = "finalv2.txt"

    # Part 1
    # Call readFile and read in finalv1.txt
    read_file(input_file, output_file)

    # Part 2
    # Takes the newly generated file and checks against the grammar
    result = check_input(output_file)
    print(result)

    # Part 3
    # If accepted by the grammar then convert the code to C++
    if result == "No error":
        convert_to_cpp(output_file)

    return 0

if __name__ == '__main__':
    main()
