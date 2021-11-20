from Stack import Stack
#put bracket validator here

def check_brackets_from_string(text):
    opening_brackets_stack = Stack()

    for char in text:

        if char == '(' or char == '[' or char == '{':
            opening_brackets_stack.push(char)
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

    if opening_brackets_stack.empty():
        return True

    return False
