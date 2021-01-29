from typing import Dict, List, Set

from test_framework import generic_test

from collections import defaultdict, deque
import string

def transform_string(D: Set[str], s: str, t: str) -> int:

    def build_adjacent_strings(string_set: Set[str]) -> Dict[str, List[str]]:
        adjacent_dict = defaultdict(list)
        while len(string_set) > 0:
            string = string_set.pop()
            for other in string_set:
                count = 0
                for pair in zip(string, other):
                    if pair[0] != pair[1]:
                        count += 1
                if count == 1:
                    adjacent_dict[string].append(other)
                    adjacent_dict[other].append(string)
        return adjacent_dict
    
    # adjacent_strings = build_adjacent_strings(D)

    def find_path(start: str):
        queue = deque([(start, 0)])
        # D.remove(start)
        while len(queue) > 0:
            (current_string, distance) = queue.popleft()
            if current_string == t:
                return distance
            if current_string not in D:
                continue
            D.remove(current_string)
            for i in range(len(current_string)):
                for letter in string.ascii_lowercase:
                    candidate = current_string[:i] + letter + current_string[(i + 1):]
                    if candidate in D:
                        # D.remove(candidate)
                        queue.append((candidate, distance + 1))
            
        return -1

    return find_path(s)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
