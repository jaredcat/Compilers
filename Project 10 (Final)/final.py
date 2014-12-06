# Pooja Srivastava & Jared Kotoff
# CS 323
# Final Project
# December 11, 2014

import sys
import re
import string


def postfix(s):
    postfixed[] = 0
    return postfixed


def readFile(infile, outfile):
    tlist = []
    g = open(outfile, "w")

    #Loop over each line in the file
    with open(infile, "r") as f:
        for line in f:

            str = " *)"
            sem = ";"

            if not line.startswith("\n"):
                # Strip the line to remove whitespace.

                line = line.strip('\t\r')
                line = line.replace("=", " = ")
                line = line.replace("+", " + ")
                line = line.replace("<<", " << ")
                line = line.replace(";", " ;")
                line = line.replace(" ,", ", ")
                line = line.replace("\t", " ")

                if str in line:
                    if sem not in line:
                        line = line.replace(line, "")

                    else:
                        line = line.replace(sem, ";\n")

                if line.startswith('\n'):
                     g.write("")

                tlist = line.split(" " or ";")

                for token in tlist:
                    if token.startswith("(*"):
                        g.write("")
                        break

                    if not token == '':

                        if not token.endswith('\n'):
                            g.write(token + " ")
                        else:
                            g.write(token)
    g.close()


def main():
    if len(sys.argv) != 4:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 <Python source code file> <input file> <output file>>')
        sys.exit(1)
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    #Part 1
    #Call readFile and read in finalv1.txt
    readFile(inputFile, outputFile)

    #Part 2
    #

    return 0