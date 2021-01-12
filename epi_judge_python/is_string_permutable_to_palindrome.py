from test_framework import generic_test
import collections

def can_form_palindrome(s: str) -> bool:
    char_count = collections.Counter(s)
    odd_counts = filter(lambda x: x % 2 == 1, char_count.values())
    return len(list(odd_counts)) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
