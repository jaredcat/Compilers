##Pooja Srivastava & Jared Kotoff
#CS 323
#Programming Assignment 2
#September 25, 2014

#!/usr/bin/python
import re

# Open this file.
f = open("testFile.txt", "r")

# Loop over each line in the file
for line in f.readlines():

    if not line.startswith("//"):
    # Strip the line to remove whitespace.
        print(line.strip(' \t\n\r'))

    # Split the line.
    line = line.split(";")

