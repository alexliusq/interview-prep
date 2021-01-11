import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    diff_xor = 0
    for x in range(len(A)):
        diff_xor = diff_xor ^ x ^ A[x]

    ## diff_xor now is the xor of missing and duplicate

    ## this is the genius part from EPI that you didn't figure out
    ## difference in bit in the diff_xor means that either the missing or
    ## duplicate has that bit set. do XOR magic for both ranges where that bit
    ## is set, and you will be able to isolate the missing or the duplicate
    set_bit = diff_xor & (~(diff_xor - 1))
    candidate = 0
    for x in range(len(A)):
        if x & set_bit:
            candidate ^= x
        if A[x] & set_bit:
            candidate ^= A[x]
    
    other = diff_xor ^ candidate
    # print('candidate', candidate, ' other:', other, 'diff_xor', diff_xor)
    if candidate in A:
        return DuplicateAndMissing(candidate, other)
    else:
        return DuplicateAndMissing(other, candidate)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
