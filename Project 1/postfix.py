#Pooja Srivastava & Jared Kotoff
#CS 323
#Programming Assignment 1
#September 11, 2014


class Stack():
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []
    
    def push(self, item):
        return self.items.append(item)
  
    def pop(self):
        return self.items.pop()
  
    def get_elements(self):
        return self.items


#function takes in string expression s and computes the value
def postfix(s):
    
    #string is broken down and stored in a list
    tlist = list(s)
    pfixstack = Stack()

    for token in tlist:
        #if a token is a letter it is asked for a int value then stored into the stack
        if token in "abcdefghijklmnopqrstuvwxyz":
            token = input("Please enter the value of " + token +": ")
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
            result = calc_result(token,value1,value2)
            #add the result onto the stack
            pfixstack.push(result)

    #final result returned to be printed		    
    return pfixstack.pop()


#Evaluates the expressions and returns a result
def calc_result(op, val1, val2):

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
    s = input("Enter a postfix expression with a $ at the end: ")

    #prints the final value of expression
    print("Final value = " + str(postfix(s)))
    c = input("Would you like to continue with a different expression? (y/n) ")