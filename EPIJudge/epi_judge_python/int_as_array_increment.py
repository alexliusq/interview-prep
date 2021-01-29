from typing import List

from test_framework import generic_test

# [1, 2, 9] -> [1,3,0]
# [9, 9] -> [1, 0, 0]
# essentially a [9] -> [1,0] problem
# so we have an increment boolean
# we exit when either increment is false or reached beginning of the array
# invariants: index is digit to increment
# if digit < 9 then increment and set increment to false
# if increment true and idx = -1, then create new array with length n + 1, set idx 0 to 1, actually rest of the array is just 0s.
# just return [1] + [existing array (which is all zeroes)] (time complexity of O(n)

def plus_one(A: List[int]) -> List[int]:
    increment = True
    next_digit = len(A) - 1
    while (increment and next_digit >= 0):
        if (A[next_digit] < 9):
            A[next_digit] += 1
            increment = False
        else:
            A[next_digit] = 0
        next_digit -= 1

    if (increment):
        # return [1] + A
        ##smarter EPI way
        A[0] = 1
        A.append(0)
    return A

def brute_force(A: List[int]) -> List[int]:
    number = int(''.join(str(x) for x in A))
    number += 1
    return [int(x) for x in list(str(number))]
    

if __name__ == '__main__':
    # print('brute force')
    # generic_test.generic_test_main('int_as_array_increment.py',
    #                                 'int_as_array_increment.tsv', brute_force)
    generic_test.generic_test_main('int_as_array_increment.py',
                                    'int_as_array_increment.tsv', plus_one)
