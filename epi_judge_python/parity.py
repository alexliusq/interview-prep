from test_framework import generic_test



def parity(x: int) -> int:
    result = 0
    while (x):
        result ^= 1
        x = x & (x - 1)
    return result

PRECOMPUTED_PARITY = [parity(x) for x in range(2**16)]

def parity_precomputed(x: int) -> int:
    BIT_MASK = 0xFFFF
    # BIT_MASK = 2^16 - 1
    result = 0
    while(x):
        result ^= PRECOMPUTED_PARITY[x & BIT_MASK]
        x >>= 16
    return result

if __name__ == '__main__':
    generic_test.generic_test_main('parity.py', 'parity.tsv', parity)
    print('Pre-computed parity')
    generic_test.generic_test_main('parity.py', 'parity.tsv', parity_precomputed)


