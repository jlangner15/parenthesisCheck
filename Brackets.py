class Brackets:
    def __init__(self, element, position):
        self.type = element
        self.posi = position

    def Match(self, ch):
        if ch == '}':
            return self.type == '{'
        if ch == ']':
            return self.type == '['
        if ch == ')':
            return self.type == '('