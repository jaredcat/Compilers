#Pooja Srivastava & Jared Kotoff
#CS 323
#Programming Assignment 2 - Part 1
#September 18, 2014


#Given a word determines if it is accepted by the language
def language(w):
    wlist = list(w)
    if wlist[0] == "a":
        for i, j in enumerate(wlist):
            if j != "a":
                if i+1 != len(wlist):
                    return "rejected"
                else:
                    return "accepted"
        return "rejected"
    elif wlist[0] == "b":
        for i in wlist:
            if i != "b":
                return "rejected"
        return "accepted"


while 1 == 1:
    #get user inputted word
    word = input("Enter word: ")
    print("The word is "+language(word))s