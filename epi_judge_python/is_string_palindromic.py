from test_framework import generic_test


# def is_palindromic(s: str) -> bool:
#     return ''.join(reversed(s)) == s

def is_palindromic(s: str) -> bool:
    ## ~i = -(i+1), REMEMBER from bit manipulation
    return all(s[i] == s[~i] for i in range(0, len(s) // 2 + 1))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
