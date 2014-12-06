# Pooja Srivastava & Jared Kotoff
# CS 323
# Final Project
# December 11, 2014

import sys
import re
import string


# Key
# [0, "PROGRAM", ";", "VAR", "BEGIN", "END.", "{", "}", ":", ", ", "INTEGER", "WRITE(", ")", "=", "+", "-", "*", "/", 
#    "(", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "$"]
table = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 
     44, 44, 44, 44, 44, 43], 
    [0, 44, 43, 44, 44, 44, 44, 44, 43, 43, 44, 44, 43, 43, 43, 43, 43, 43, 44, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 
     2, 2, 44], 
    [0, 44, 44, 44, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
     4, 4, 44], 
    [0, 44, 44, 44, 44, 44, 44, 44, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
     6, 6, 44], 
    [0, 44, 43, 44, 44, 44, 44, 44, 44, 44, 7, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 
     44, 44, 44, 44, 44, 44], 
    [0, 44, 44, 44, 44, 43, 44, 44, 44, 44, 44, 9, 44, 44, 44, 44, 44, 44, 44, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 
     9, 9, 44], 
    [0, 44, 44, 44, 44, 43, 44, 44, 44, 44, 44, 10, 44, 44, 44, 44, 44, 44, 44, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 
     11, 11, 11, 11, 11, 44], 
    [0, 44, 44, 44, 44, 43, 44, 44, 44, 44, 44, 12, 44, 44, 44, 44, 44, 44, 44, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 
     43, 43, 43, 43, 43, 44], 
    [0, 44, 44, 44, 44, 43, 44, 44, 44, 44, 44, 43, 44, 44, 44, 44, 44, 44, 44, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 
     13, 13, 13, 13, 13, 44], 
    [0, 44, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 43, 44, 16, 16, 44, 44, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 
     16, 16, 16, 16, 16, 44], 
    [0, 44, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 43, 44, 17, 17, 44, 44, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 
     17, 17, 17, 17, 17, 44], 
    [0, 44, 20, 44, 44, 44, 44, 44, 44, 44, 44, 44, 20, 44, 20, 20, 18, 19, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 
     44, 44, 44, 44, 44, 44], 
    [0, 44, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 43, 44, 22, 22, 43, 43, 23, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 
     21, 21, 21, 21, 21, 44], 
    [0, 44, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 43, 44, 24, 24, 43, 43, 44, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 
     44, 44, 44, 44, 44, 44], 
    [0, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 25, 26, 44, 44, 44, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 
     44, 44, 44, 44, 44, 44], 
    [0, 44, 44, 44, 44, 44, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 
     44, 44, 44, 44, 44, 44], 
    [0, 44, 43, 44, 44, 44, 43, 44, 43, 43, 44, 44, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 
     38, 39, 40, 41, 42, 44]
]


def lookup(input):
    colums = [0, "PROGRAM", ";", "VAR", "BEGIN", "END.", "{", "}", ":", ", ", "INTEGER", "WRITE(", ")", "=", "+",
              "-", "*", "/", "(", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "$"]
    rows = [0, ""]
    return look_up_table.index(input)


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
    stack.append('E')
    print_stack(stack)

    with open(file, "r") as f:
        while stack:
            line = f.split(" " or ";")
            # if line ends before the stack is empty then reject
            if len(stack) != 0 and len(line) - i == 0:
                return 'Rejected'

            # Looks at the last item in the stack
            token = stack[len(stack)-1]
            # First item in the input
            read = line[i]

            # If the token is terminal
            if token in tokens:
                # if the token is the same as the one from the input
                if token == read:
                    stack.pop()
                    print_stack(stack)
                    i += 1
                else:
                    # terminal token but not the same
                    return 'Rejected'
            else:  # Token is non-terminal
                lookup = table(token, read)
                if lookup == '%':  # if lamda
                    stack.pop()
                elif lookup: # if not empty
                    stack.pop()
                    for j in reversed(lookup):
                        stack.append(j)
                else:
                    return 'Rejected'
    return 'Accepted'


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
