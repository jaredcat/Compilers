##Pooja Srivastava & Jared Kotoff
#CS 323
#Programming Assignment 6
#October 9, 2014

#Tokens separated by class
classify = ([
    ["type", "int", "float"],
    ["reserved word", "main", "cout<<"],
    ["operator", "+", "-", "*", "/", "="],
    ["separator", "(", ")", ";", "{", "}", ")", ","]
])

tokens = ['a', '+', '-', '*', '/', '(', ')', '$']


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


def check_input(line):
    i = 0
    stack = ([])
    stack.append('$')
    stack.append('E')
    while stack:
        print(stack)

        token = stack[len(stack)-1]
        read = line[i]

        if token in tokens:
            if token == read:
                stack.pop()
                i += 1
            else:
                return "Rejected"
        else:
            lookup = table(token, read)
            if lookup == '%':
                stack.pop()
            elif lookup != '':
                stack.pop()
                for j in reversed(lookup):
                    stack.append(j)
            else:
                return "Rejected"
    return 'Accepted'


def main():
    line = input()
    print(check_input(line))

if __name__ == '__main__':
    main()