import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    result_size = 0
    for i in range(size):
        if s[i] != 'b':
            s[result_size] = s[i]
            result_size += 1
    count_a = s[:result_size].count('a')
    full_size = result_size + count_a
    idx = result_size - 1
    while count_a > 0:
        if s[idx] != 'a':
            s[idx + count_a] = s[idx]
        else:
            s[idx + count_a] = 'd'
            count_a -= 1
            s[idx + count_a] = 'd'
        idx -= 1
    return full_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
