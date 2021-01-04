from test_framework import generic_test
from test_framework.test_failure import TestFailure


## 1234
## digit = 4, [4], 123
## digit = 3, [4,3], 12
## digit = 2, [4,3,2], 1
## digit = 1, [4,3,2,1], 1

def int_to_string(x: int) -> str:
    digit_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    stringified = []
    negative = False
    if x == 0:
        return '0'
    if x < 0:
        negative = True
        x = -x
    while x > 0:
        digit = x % 10
        stringified.append(digit_array[digit])
        x //= 10
    if negative:
        stringified.append('-')
    return ''.join(reversed(stringified))


## '12340'
## range(5) -> [0,1,2,3,4]
## 1 * 10^4 + 2 * 10^3 + 3 * 10 ^ 2 + 4 * 10 ^ 1 + 0 * 10^0

def string_to_int(s: str) -> int:
    string_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9   
    }
    str_length = len(s)
    result_int = 0
    is_negative = False
    for i in range(str_length):
        if s[i] == '-':
            is_negative = True
            continue
        if s[i] == '+':
            continue
        result_int += string_dict.get(s[i]) * (10 ** (str_length - 1 - i))
    return -result_int if is_negative else result_int


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
