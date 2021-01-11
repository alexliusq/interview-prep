from test_framework import generic_test


def square_root(k: int) -> int:
    start = 0
    end = k
    while start <= end:
        middle = (start + end) // 2
        if middle ** 2 > k:
            end = middle - 1
        else:
            ## middle ** 2 <= k
            start = middle + 1
    return start - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
