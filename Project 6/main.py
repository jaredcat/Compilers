##Pooja Srivastava & Jared Kotoff
#CS 323
#Programming Assignment 3
#September 25, 2014

#!/usr/bin/python
import re
import string

# Open this file.
f = open("data.txt", "r")
g = open("newdata.txt", "w")
tlist = []

#Tokens seperated by class
identifier = set(string.ascii_letters)
constants = set(string.digits)
seperators = ["(", ")", ";", "{", "}", ")"]
operators = ["+", "-", "*", "/"]
types = ["int", "float"]
reserved_words = ["main", "count<<"]

# Loop over each line in the file
for line in f.readlines():

    if not line.startswith("//") and not line.startswith("\n"):
        # Strip the line to remove whitespace.
        line = line.strip(' \t\r')
        line = line.replace("=", " = ")
        line = line.replace("+", " + ")
        line = line.replace("<<", " << ")
        line = line.replace(";", " ;")
        line = line.replace(" ,", ", ")
        for token in tlist:
            if token.startswith("//"):
                g.write("\n")
                break
            if not token == '':
                if not token.endswith('\n'):
                    g.write(token + " ")
                else:
                    g.write(token)