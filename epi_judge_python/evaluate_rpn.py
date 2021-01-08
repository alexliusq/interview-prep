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

    for token in parsed:
        if token in operations:
            y = stack.pop()
            x = stack.pop()
            result = operations[token](x, y)
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
