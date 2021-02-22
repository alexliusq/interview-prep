
from collections import namedtuple

Frame = namedtuple('Frame', ['is_arg', 'value'])

def fib_with_stack(n):

    stack = []
    stack.append(Frame(True, n))

    while len(stack) >=2 or stack[-1].is_arg:
        print(stack)
        is_arg, value = stack.pop()
        if is_arg:
            if value < 2:
                stack.append(Frame(False, value))
            else:
                stack.append(Frame(True, value - 1))
                stack.append(Frame(True, value - 2))
        else:
            prev_is_arg, prev_value = stack.pop()
            if prev_is_arg:
                stack.append(Frame(False, value))
                stack.append(Frame(True, prev_value))
            else:
                stack.append(Frame(False, value + prev_value))
    
    print(stack)
    return stack[0].value



print(fib_with_stack(10))