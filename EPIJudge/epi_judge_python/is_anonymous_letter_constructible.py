from test_framework import generic_test
import collections

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    magazine_counter = collections.Counter(magazine_text)
    letter_counter = collections.Counter(letter_text)
    # print(letter_counter - magazine_counter)
    return len(letter_counter - magazine_counter) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
