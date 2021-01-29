from test_framework import generic_test

def reverse_bit_brute_force(x: int) -> int:
    reversed_int = 0
    for i in range(64):
        reversed_int <<= 1
        reversed_int |= (x & 1)
        x >>= 1
    return reversed_int

def reverse_16(x: int) -> int:
    reversed_int = 0
    for i in range(16):
        reversed_int <<= 1
        reversed_int |= (x & 1)
        x >>= 1
    return reversed_int

REVERSE_LOOKUP = [reverse_16(x) for x in range(2 ** 16)]

def reverse_bit(x: int) -> int:
    reversed_int = 0
    mask = 0xFFFF
    for i in range(4):
        reversed_int <<= 16
        # print(str(mask & x))
        # print(str(i) + ' ' + str(REVERSE_LOOKUP[mask & x]))
        reversed_int |= REVERSE_LOOKUP[mask & x]
        # print(str(i) + ' ' + bin(reversed_int))
        x >>= 16
    return reversed_int

if __name__ == '__main__':
    print('brute force')
    generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                    reverse_bit_brute_force)
    print('lookup table')
    generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                    reverse_bit)
