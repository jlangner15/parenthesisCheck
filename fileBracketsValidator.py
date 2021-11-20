from Stack import Stack


def checkFile(input):
    f = open(input, 'r')

    outStr = ""

    opening_brackets_stack = Stack()

    for line in f:
        for char in line:
            if char in ['(', '[', '{']:
                opening_brackets_stack.push(char)
            elif char not in [')', '}', ']']:
                pass
            else:
                if opening_brackets_stack.size() > 0:

                    peek = opening_brackets_stack.peek()
                    opening_brackets_stack.pop()

                    if peek == '(' and char != ')':
                        return False
                    if peek == '{' and char != '}':
                        return False
                    if peek == '[' and char != ']':
                        return False
                else:
                    return False

    f.close()

    if opening_brackets_stack.empty():
        return True

    return False