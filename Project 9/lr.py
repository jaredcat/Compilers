##Pooja Srivastava & Jared Kotoff
#CS 323
#Programming Assignment 9
#November 13, 2014


#Predictive parsing table
##[0-15], [0 1 2 3 4 5 6 7 8 9 10] Row #'s
##[0-15], [i + - * / ( ) $ E T F] Translation
table = [
    [105, 0, 0, 0, 0, 104, 0, 0, 1, 2, 3],
    [0, 106, 107, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 203, 203, 108, 109, 0, 203, 203, 0, 0, ],
    [0, 206, 206, 206, 206, 0, 206, 206, 0, 0, 0],
    [105, 0, 0, 0, 0, 104, 0, 0, 10, 2, 3],
    [0, 208, 208, 208, 208, 0, 208, 208, 0, 0, 0],
    [105, 0, 0, 0, 0, 104, 0, 0, 0, 11, 3],
    [105, 0, 0, 0, 0, 104, 0, 0, 0, 12, 3],
    [105, 0, 0, 0, 0, 104, 0, 0, 0, 0, 13],
    [105, 0, 0, 0, 0, 104, 0, 0, 0, 0, 14],
    [0, 106, 107, 0, 0, 0, 115, 0, 0, 0, 0],
    [0, 201, 201, 108, 109, 0, 201, 201, 0, 0, 0],
    [0, 202, 202, 108, 109, 0, 202, 202, 0, 0, 0],
    [0, 204, 204, 204, 204, 0, 204, 204, 0, 0, 0],
    [0, 205, 205, 205, 205, 0, 205, 205, 0, 0, 0],
    [0, 207, 207, 207, 207, 0, 207, 207, 0, 0, 0]
]
#The language [x][0] for left-hand side, [x][1] for right-hand side
language = [["E", "E+T"], ["E", "E-Y"], ["E", "T"], ["T", "T*F"], ["T", "T/F"], ["T", "F"], ["F", "(E)"], ["F", "i"]]


#Function to print the current stack to terminal
def print_stack(stack):
    print('Stack: ', end='')
    for i in stack:
        print(i, end='')
    print()


def convert_token(token):
    tokens = ["i", "+", "-", "*", "/", "(", ")", "$", "E", "T", "F"]
    return tokens.index(token)


#Traces the input
def check_input(line):
    i = 0
    stack = ([])
    stack.append('0')
    print_stack(stack)

    while stack:
        #Looks at the last item in the stack
        item = int(stack.pop())
        #First item in the input
        token = line[i]

        table_lookup = table[item][convert_token(token)]
        if table_lookup > 200:
            #subtract an extra one because of array indexing
            table_lookup -= 201
            stack.append(item)
            #looks up the grammar in the language
            language_lookup = language[table_lookup]
            #pop 2*|length of grammar (LHS)|
            for j in range(0, len(language_lookup[1])):
                stack.pop()
                stack.pop()
            item = stack.pop()
            #Push RHS of grammar to stack
            token = language_lookup[0]
            stack.append(item)
            stack.append(token)
            stack.append(table[item][convert_token(token)])
        elif 200 > table_lookup > 100:
            table_lookup -= 100
            stack.append(item)
            stack.append(token)
            stack.append(table_lookup)
            i += 1
        elif table_lookup == 1:
            return 'Accepted'
        else:
            return 'Rejected'
        print_stack(stack)
    return 'Rejected'


def main():
    line = input()
    print(check_input(line))


if __name__ == '__main__':
    main()