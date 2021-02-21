


class StackOfPlatesException(Exception):
    pass

class EmptyStackException(StackOfPlatesException):
    pass

class StackOfPlates:

    def __init__(self, max_size):
        self.max_size = max_size
        self.stacks = []

    def push(self, value):
        if not self.stack or len(self.stacks[-1]) == self.max_size:
            self.stack.append([value])
        else:
            self.stacks[-1].append(value)
    
    def pop(self):
        if self.stacks[-1]:
            return self.stacks[-1].pop()
        else:
            self.stacks.pop()
            if self.stacks:
                return self.stacks[-1].pop()
            else:
                raise EmptyStackException

