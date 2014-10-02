##Pooja Srivastava & Jared Kotoff
#CS 323
#Programming Assignment 6
#October 9, 2014


# Open this file.
f = open("data.txt", "r")
g = open("newdata.txt", "w")
tlist = []

#Tokens separated by class
classify = ([
    ["type", "int", "float"],
    ["reserved word", "main", "cout<<"],
    ["operator", "+", "-", "*", "/", "="],
    ["separator", "(", ")", ";", "{", "}", ")", ","]
])

# Loop over each line in the file
for line in f.readlines():
    #Skips lines that are comments or blank
    if not line.startswith("//") and not line.startswith("\n"):
        # Strip the line to remove whitespace.
        line = line.strip(' \t\r')
        #Correts formatting
        line = line.replace(";", " ; ")
        line = line.replace("{", " { ")
        line = line.replace("cout<<", "cout<< ")
        #Slips the line up into segments separated by spaces
        tlist = line.split(" ")
        for token in tlist:
            #Sets flag back to false
            next_token = 0
            #Check for a comment at the end of the line
            if token.startswith("//"):
                g.write("\n")
                break
            #Check if the token is empty
            elif not token == '':
                #Cycles though all the classes
                for i in range(0, len(classify)):
                    #Checks if the token has been given a class already
                    if next_token:
                        break
                    #Cycles though all the objects in a class
                    for j in range(1, len(classify[i])):
                        if token == classify[i][j]:
                            g.write(token + "    " + classify[i][0] + "\n")
                            next_token = 1
                            break
                #If object has not been given a class
                if not next_token:
                    #If the token starts with a number then it must be a constant/digit
                    if token[0].isdigit():
                        g.write(token + "    constant" + "\n")
                    #If the token stats with a letter than it must be an identifier
                    elif token[0].isalpha():
                        g.write(token + "    identifier" + "\n")