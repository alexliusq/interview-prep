from typing import Iterator

from test_framework import generic_test
from collections import Counter

# def majority_search(stream: Iterator[str]) -> str:
#     string_count = Counter() 
#     for token in stream:
#         # print(token)
#         string_count[token] += 1
#     # print(list(string_count))
#     most_common = string_count.most_common(1)
#     # print(most_common)
#     return most_common[0][0]

## genius epi way
def majority_search(stream: Iterator[str]) -> str:
    count = 1
    candidate = ''
    for next_string in stream:
        if next_string != candidate:
            count -= 1
            if count == 0:
                candidate = next_string
                count = 1
        else:
            count += 1
    return candidate


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
