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

#Alpa holds a set of letters
alpha = set(string.ascii_letters)

#Num holds a set of digits
num = set(string.digits)
#symb holds a set of symbols and punctuation
symb = set(string.punctuation)

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
        tlist = line.split(" " or ";")
        for token in tlist:
            if token.startswith("//"):
                g.write("\n")
                break
            if not token == '':
                if not token.endswith('\n'):
                    g.write(token + " ")
                else:
                    g.write(token)