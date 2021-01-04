from test_framework import generic_test

import string

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    hexdigits = '0123456789ABCDEF'
    base_10 = 0
    num_as_string = num_as_string.upper()
    is_negative = False
    for i in range(len(num_as_string)):
        if num_as_string[i] == '-':
            is_negative = True
            continue
        digit = hexdigits.index(num_as_string[i])
        base_10 = base_10 * b1 + digit
    # print(base_10)
    converted = []
    while True:
        digit = base_10 % b2
        converted.append(hexdigits[digit])
        base_10 = (base_10 - digit) // b2
        if base_10 == 0:
            break

    if is_negative:
        converted.append('-')
    return ''.join(reversed(converted))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
