from functools import cached_property
from typing import List

from test_framework import generic_test

from collections import defaultdict

def find_nearest_repetition(paragraph: List[str]) -> int:
    char_locations = defaultdict(list)
    for index, word in enumerate(paragraph):
        char_locations[word].append(index)

    char_differences = {}
    # print(char_locations)
    for word in char_locations:
        differences = [end - start for end, start in
                        zip(char_locations[word][1:], char_locations[word][:-1])]
        # print(differences)
        if differences:
            char_differences[word] = min(differences)
    # print(char_differences)
    if char_differences:
        return min(difference for difference in char_differences.values())
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
