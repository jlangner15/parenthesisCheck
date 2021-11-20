from Stack import Stack
from Brackets import Brackets

def brackets_validator(str):
    flag = True
    opening_bracket_stack = Stack()

    position = 0
    for ch in str:
        position += 1
        if (ch == '(' or ch == '[' or ch == '{'):
            temp = Brackets(ch, position)
            opening_bracket_stack.push(temp)

        if (ch == ')' or ch == ']' or ch == '}'):
            if opening_bracket_stack.empty():
                flag = False
                temp = Brackets(ch, position)
                opening_bracket_stack.push(temp)
                break
            elif (not opening_bracket_stack.top().Match(ch)):
                flag = False
                temp = Brackets(ch, position)
                opening_bracket_stack.push(temp)
                break
            else :
                opening_bracket_stack.pop()

    if (opening_bracket_stack.empty() and flag):
        #print("Success")
        return -1
    else :
        #print(opening_bracket_stack.top().posi)
        return opening_bracket_stack.top().posi
