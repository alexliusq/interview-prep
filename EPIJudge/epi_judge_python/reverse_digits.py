from test_framework import generic_test

def reverse_with_string(x: int) -> int:
    absolute_x = str(abs(x))
    reversed_list = [absolute_x[i] for i in range(len(absolute_x) - 1, -1, -1)]
    reversed_int = int(''.join(reversed_list))
    return -reversed_int if x < 0 else reversed_int

def reverse(x: int) -> int:
    absolute_x = abs(x)
    reversed_int = 0
    while(absolute_x > 0):
        reversed_int = reversed_int * 10 + (absolute_x % 10)
        absolute_x //= 10
    return -reversed_int if x < 0 else reversed_int


if __name__ == '__main__':
    print('string method')
    generic_test.generic_test_main('reverse_digits.py',
                                    'reverse_digits.tsv',
                                    reverse_with_string)
    print('modulus method')
    generic_test.generic_test_main('reverse_digits.py',
                                    'reverse_digits.tsv',
                                    reverse)
