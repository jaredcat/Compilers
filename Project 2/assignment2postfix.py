#Pooja Srivastava & Jared Kotoff
#CS 323
#Programming Assignment 2
#September 18, 2014


class Stack():
    def __init__(myStack):
        myStack.items = []

    def isEmpty(myStack):
        return myStack.items == []

    def push(myStack, item):
        return myStack.items.append(item)

    def pop(myStack):
        return myStack.items.pop()

    def getelements(myStack):
        return myStack.items


#function takes in string expression s and computes the value
def postfix(s):

    import string

    #string is broken down and stored in a list
    tlist = s.split(" ")
    pfixstack = Stack()

    #Alpa holds a set of letters
    alpha = set(string.ascii_letters)

    #Num holds a set of digits
    num = set(string.digits)

    for token in tlist:

        #if a token begins with a letter it is asked for a int value then pushed into the stack
        if token.startswith((tuple(alpha))):
            token = input("Please enter the value of " + token + ": ")
            pfixstack.push(int(token))

        #If token contains digits they are immediately pushed into the stack
        elif set(token) <= num:
            pfixstack.push(int(token))


        #handles the $ at the end. Pushes it then pops it from the stack
        elif token == '$':
            pfixstack.push(token)
            pfixstack.pop()

        #if the token is an operator it will be popped from the stack
        else:
            value2 = pfixstack.pop()
            value1 = pfixstack.pop()
            #to calculate the result of each operation
            result = calcresult(token,value1,value2)
            #add the result onto the stack
            pfixstack.push(result)

    #final result returned to be printed
    return pfixstack.pop()


#Evaluates the expressions and returns a result
def calcresult(op, val1, val2):

    if op == "*":
        return val1 * val2
    elif op == "/":
        return val1 / val2
    elif op == "+":
        return val1 + val2
    else:
        return val1 - val2

#loop control variable
c = 'y'

while c == 'y':
    #get user input of expression
    s = eval(input("Enter a postfix expression with a $ at the end: "))

    #prints the final value of expression
    print("Expression value is:  " + str(postfix(s)))
    c = input("CONTINUE? (y/n) ")