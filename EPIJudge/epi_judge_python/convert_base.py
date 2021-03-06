from test_framework import generic_test

import string

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    

    hexdigits = '0123456789ABCDEF'
    base_10 = 0
    num_as_string = num_as_string.upper()
    is_negative = False

    def build_from_base(num: int, base: int) -> str:
        digit = num % base
        num = (num - digit) // base
        digit_str = hexdigits[digit]
        if num == 0:
            return digit_str
        return build_from_base(num, base) + digit_str

    for i in range(len(num_as_string)):
        if num_as_string[i] == '-':
            is_negative = True
            continue
        digit = hexdigits.index(num_as_string[i])
        base_10 = base_10 * b1 + digit
    # print(base_10)
    ## old looping method, implement fancy recursive method
    # converted = []
    # while True:
    #     digit = base_10 % b2
    #     converted.append(hexdigits[digit])
    #     base_10 = (base_10 - digit) // b2
    #     if base_10 == 0:
    #         break

    result = build_from_base(base_10, b2)
    if is_negative:
        result = '-' + result
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
