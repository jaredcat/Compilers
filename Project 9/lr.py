##Pooja Srivastava & Jared Kotoff
#CS 323
#Programming Assignment 6
#October 9, 2014


#Potential terminal tokens for this language
tokens = ['a', '+', '-', '*', '/', '(', ')', '$']


#Predictive parsing table
def table(nonterminal, terminal):
    if nonterminal == 'E':
        if terminal == 'a' or terminal == '(':
            return 'TQ'
    elif nonterminal == 'Q':
        if terminal == '+':
            return '+TQ'
        elif terminal == '-':
            return '-TQ'
        elif terminal == ')' or terminal == '$':
            return '%'
    elif nonterminal == 'T':
        if terminal == 'a' or terminal == '(':
            return 'FR'
    elif nonterminal == 'R':
        if terminal == '+' or terminal == '-' or terminal == ')' or terminal == '$':
            return '%'
        if terminal == '*':
            return '*FR'
        if terminal == '/':
            return '/FR'
    elif nonterminal == 'F':
        if terminal == 'a':
            return 'a'
        if terminal == '(':
            return '(E)'
    else:
        return ''


#Function to print the current stack to terminal
def print_stack(stack):
    print('Stack: ', end='')
    for i in stack:
        print(i, end='')
    print()


#Traces the input
def check_input(line):
    i = 0
    stack = ([])
    stack.append('$')
    stack.append('E')
    print_stack(stack)

    while stack:
        #if line ends before the stack is empty then reject
        if (len(stack) != 0 and len(line) - i == 0):
            return 'Rejected'

        #Looks at the last item in the stack
        token = stack[len(stack)-1]
        #First item in the input
        read = line[i]

        #If the token is terminal
        if token in tokens:
            #if the token is the same as the one from the input
            if token == read:
                stack.pop()
                print_stack(stack)
                i += 1
            else:
                #terminal token but not the same
                return 'Rejected'
        else: #Token is non-terminal
            lookup = table(token, read)
            if lookup == '%': #if lamda
                stack.pop()
            elif lookup: #if not empty
                stack.pop()
                for j in reversed(lookup):
                    stack.append(j)
            else:
                return 'Rejected'
    return 'Accepted'


def main():
    line = input()
    print(check_input(line))


if __name__ == '__main__':
    main()