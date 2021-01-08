from typing import List
from test_framework import generic_test


def evaluate(expression: str) -> int:
    i = 0
    stack = []
    operations = {
        '*': lambda x, y: x * y,
        '/': lambda x, y: x //y,
        '+': lambda x, y: x + y,
        '-': lambda x, y: x -y
    }
    parsed = expression.split(',')

    while i < len(parsed):
        element = parsed[i]
        i += 1
        if element in operations:
            y = int(stack.pop())
            x = int(stack.pop())
            result = operations[element](x, y)
            stack.append(result)
        else:
            stack.append(int(element))
    return stack[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
