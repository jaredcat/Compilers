# Pooja Srivastava & Jared Kotoff
# CS 323
# Final Project
# December 11, 2014

import sys
import re
import string


# Key
# [0, "PROGRAM", ";", "VAR", "BEGIN", "END.", "{", "}", ":", ",", "INTEGER", "WRITE(", ")", "=", "+", "-", "*", "/",
# "(", "DIGITS", "LETTERS", "$"]
table = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 11, 11, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 13, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 16, 0, 0, 16, 16, 16, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 17, 0, 0, 17, 17, 17, 0],
    [0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 20, 20, 18, 19, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 22, 0, 0, 23, 22, 21, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 24, 0, 0, 0, 24, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 26, 0, 0, 0, 27, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 0]
]
columns = [0, "PROGRAM", ";", "VAR", "BEGIN", "END.", "{", "}", ":", ", ", "INTEGER", "WRITE(", ")", "=", "+",
           "-", "*", "/", "(", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "$"]
rows = [0, "program", "identifier", "dec-list", "dec", "type", "stat-list", "stat", "write", "assign", "expr",
        "term", "termtail", "factor", "number", "sign", "digit", "id"]

reserved_words = ["PROGRAM", "VAR", "BEGIN", "END.", "INTEGER", "WRITE"]
predictive_set = [0, ["PROGRAM"], ["LETTERS"], ["DIGITS"], ["LETTERS", "DIGITS"], ["LETTERS", "DIGITS"],
                  ["LETTERS", "DIGITS"], ["INTEGER"], ["WRITE(", "LETTERS", "DIGITS"], ["WRITE(", "LETTERS", "DIGITS"],
                  ["WRITE("], ["LETTERS", "DIGITS"], ["WRITE("], ["LETTERS", "DIGITS"],
                  ["(", "LETTERS", "DIGITS", "+", "-"], ["(", "LETTERS", "DIGITS", "+", "-"],
                  ["(", "LETTERS", "DIGITS", "+", "-"], ["(", "LETTERS", "DIGITS", "+", "-"], ["*"], ["/"],
                  ["+", "-", ")", ";"], ["LETTERS", "DIGITS"], ["+", "-", "DIGITS"], ["("], ["+", "-", "DIGITS"],
                  ["+"], ["-"], ["DIGITS"], ["DIGITS"], ["LETTERS"]]


def readfile(infile, outfile):
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
                line = line.replace(" , ", ", ")
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
    i = 0
    stack = ([])
    stack.append('$')
    stack.append(rows.index("program"))
    print_stack(stack)

    with open(file, "r") as f:
        for line in f:
            while stack:
                line = line.split(" ")

                #Looks at the last item in the stack
                token = rows.index(stack[len(stack)-1])
                #First item in the input
                read = columns.index(line[i])

                parse = table[token][read]
                if parse




# Function to print the current stack to terminal
def print_stack(stack):
    print('Stack: ', end='')
    for i in stack:
        print(i, end='')
    print()


def main():
    if len(sys.argv) != 3:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 <Python source code file> <input file> <output file>>')
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Part 1
    # Call readFile and read in finalv1.txt
    readfile(input_file, output_file)

    #Part 2
    check_input(output_file)

    return 0

if __name__ == '__main__':
    main()
