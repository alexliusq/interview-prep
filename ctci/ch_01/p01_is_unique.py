import unittest
from collections import Counter

# def is_unique(s: str) -> bool:
#     if len(s) >= 128:
#         return False
    
#     # return all(count <= 1 for count in Counter(s).values())
#     return False

def is_unique(s: str) -> bool:
    char_seen = [False for _ in range(128)]
    for char in s:
        char_index = ord(char)
        if char_seen[char_index]:
            return False
        char_seen[char_index] = True
    
    return True


test_cases = [
    ('11123', False),
    ('abdd', False),
    ('abcd', True),
    ('1234', True)
]

for case in test_cases:
    input_val, expected = case
    assert is_unique(input_val) == expected, f"FAILED for {input_val}"

# class TestUnique(unittest.TestCase):

#     def test_unique(self):
#         test_cases = [
#             ('11123', False),
#             ('abdd', False),
#             ('abcd', True),
#             ('1234', True)
#         ]
#         for case in test_cases:
#             test_string, expected = case
#             self.assertEqual(is_unique(test_string), expected,
#                 msg=f"Failed for: {test_string}")
        

# if __name__ == "__main__":
#     unittest.main(verbosity=2)