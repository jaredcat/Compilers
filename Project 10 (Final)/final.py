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
table = [
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
columns = [0, "PROGRAM", ";", "VAR", "BEGIN", "END.", ":", ",", "INTEGER", "WRITE", "(", ")", "=", "+", "-", "*", "/",
           "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "$"]
rows = [0, "program", "identifier", "identifiertail", "dec-list", "dec", "dectail", "type", "stat-list",
        "stat-listtail", "stat", "write", "assign", "expr", "exprtail", "term", "termtail", "factor", "number",
        "numbertail", "sign", "digit", "id"]
DIGITS = ["DIGITS", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
LETTERS = ["LETTERS", "a", "b", "c", "d", "e"]
SYMBOLS = [",", ";", ":", "(", ")", "-", "+", "-", "*", "/", "="]

reserved_words = ["PROGRAM", "VAR", "BEGIN", "END.", "INTEGER", "WRITE"]
predictive_set = [0, ["PROGRAM", "identifier", ";", "VAR", "dec-list", "BEGIN", "stat-list", "END."],
                  ["id", "identifiertail"], ["id", "identifiertail"], ["digit", "identifiertail"], ["λ"],
                  ["dec", ":", "type", ";"], ["identifier", "dectail"], [",", "dec"], ["λ"], ["INTEGER"],
                  ["stat", "stat-listtail"], ["stat-list"], ["λ"], ["write"], ["assign"],
                  ["WRITE", "(", "identifier", ")", ";"], ["identifier", "=", "expr", ";"], ["term", "exprtail"],
                  ["+", "expr"], ["-", "expr"], ["λ"], ["factor", "termtail"], ["*", "factor", "termtail"],
                  ["/", "factor", "termtail"], ["λ"], ["identifier"], ["number"], ["(", "expr", ")"],
                  ["sign", "digit", "numbertail"], ["digit", "numbertail"], ["λ"], ["+"], ["-"], ["λ"], ["0"], ["1"],
                  ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["a"], ["b"], ["c"], ["d"], ["e"]]


def read_file(infile, outfile):
    t_list = []
    g = open(outfile, "w")

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
                line = line.replace("WRITE(", "WRITE (")
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
    g.close()


# Traces the input
def check_input(file):
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

                if token == "$" and not read:
                    return "Accepted"
                elif token in LETTERS or token in DIGITS or token in SYMBOLS or token in reserved_words:
                    if token == read:
                        i += 1
                    elif token == read[k][0]:
                        k += 1
                        if k == len(read):
                            i += 1
                            k = 0
                    elif token in reserved_words:
                        print("\n" +token + " is expected")
                        print(read + " was provided" + "\n")
                        return "Rejected"
                    else:
                        return "Rejected"
                    if i == len(line):
                            next_line = True
                else:
                    if read[k][0] in LETTERS or read[k][0] in DIGITS:
                        column = columns.index(read[k][0])
                    else:
                        column = columns.index(read)
                    row = rows.index(token)
                    parse = table[row][column]
                    parse = predictive_set[parse]

                    if parse != ['λ']:
                        if parse == 0:
                            return "Rejected"
                        for j in range(len(parse)-1, -1, -1):
                            stack.append(parse[j])
                        print_stack(stack)


# Function to print the current stack to terminal
def print_stack(stack):
    print('Stack: ', end='')
    for i in stack:
        print(i + " ", end='')
    print()


def print_array(array):
    for i in array:
        print("    " + i, end='')
    print()


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
            if "INTEGER" in line:
                print("    int ", end='')
                for i in line:
                    if i == ":":
                        print(" ;")
                        break
                    else:
                        print(" " + i, end='')
            elif "BEGIN" in line:
                1 == 1
            elif "WRITE" in line:
                print("    cout<< ", end='')
                for i in line:
                    if i == "WRITE" or i == "(":
                        1 == 1
                    elif i != ")":
                        print(i + " << ", end='')
                    else:
                        print("endl ;")
                        break
            elif "END." in line:
                print("    return 0;")
                break
            else:
                print_array(line)
        print("}")
    return 0


def main():
    # if len(sys.argv) != 3:
    #    print('error: you must supply exactly two arguments\n\n' +
    #          'usage: python3 <Python source code file> <input file> <output file>>')
    #    sys.exit(1)
    # input_file = sys.argv[1]
    # output_file = sys.argv[2]
    input_file = "finalv1.txt"
    output_file = "finalv2.txt"

    # Part 1
    # Call readFile and read in finalv1.txt
    read_file(input_file, output_file)

    #Part 2
    result = check_input(output_file)
    print(result)

    #Part 3
    if result == "Accepted":
        convert_to_cpp(output_file)

    return 0

if __name__ == '__main__':
    main()
