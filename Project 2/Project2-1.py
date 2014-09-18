#Pooja Srivastava & Jared Kotoff
#CS 323
#Programming Assignment 2 - Part 1
#September 18, 2014


#Given a word determines if it is accepted by the language
def language(w):
    wlist = list(w)
    #if the first letter is "a"
    if wlist[0] == "a":
        #loop though all letters in input
        for i, j in enumerate(wlist):
            #lets a* loop.
            if j != "a":
                if i+1 != len(wlist):
                    return "rejected"
                elif j == "b":
                    return "accepted"
        return "rejected"
    #if the first letter is "b"
    elif wlist[0] == "b":
        for i in wlist:
            #the word can only contain "b"
            if i != "b":
                return "rejected"
        #the word is composed of only 'B's and is accepted
        return "accepted"
    #no valid input found
    return "rejected"



while 1 == 1:
    #get user inputted word
    word = input("Enter word: ")
    #prints out if the word is accepted or not
    print("The word is "+language(word))