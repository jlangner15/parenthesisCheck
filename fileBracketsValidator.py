from Stack import Stack

'''
Returns -1 if True
else it wil return the index of the character where it failed
'''
def checkFile(input):
    f = open(input, 'r')

    opening_brackets_stack = Stack()

    index = 0 #count chars in the string to return failure index

    for line in f:
        for char in line:
            index += 1
            if char in ['(', '[', '{']:
                opening_brackets_stack.push(char)
            elif char not in [')', '}', ']']:
                pass
            else:
                if opening_brackets_stack.size() > 0:

                    peek = opening_brackets_stack.peek()
                    opening_brackets_stack.pop()

                    if peek == '(' and char != ')':
                        return index
                    if peek == '{' and char != '}':
                        return index
                    if peek == '[' and char != ']':
                        return index
                else:
                    return index

    f.close()

    if opening_brackets_stack.empty():
        return -1

    return index