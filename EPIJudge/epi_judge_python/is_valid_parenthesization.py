from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    tokenized = list(s)
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    left_brackets = []
    for token in tokenized:
        if token in brackets:
            left_brackets.append(token)
        else:
            if len(left_brackets) == 0:
                return False
            if brackets[left_brackets.pop()] != token:
                return False
    return len(left_brackets) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
