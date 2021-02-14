import random
from collections import Counter

##O(n) space use Counter, O(n) time
## O(nlogn) time, O(1) space, sort and linearly scan

## ASK ABOUT whitespace and case!

def is_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    return Counter(s1) == Counter(s2)

sample_strings = [
    'aabb',
    'aabbc'
    'a',
    'abc'
    '',
]

def test_true():
    for val in sample_strings:
        shuffled = list(val)
        random.shuffle(shuffled)
        shuffled = ''.join(shuffled)
        assert is_permutation(val, shuffled) == True, f"Failed for val: {val}"

test_true()