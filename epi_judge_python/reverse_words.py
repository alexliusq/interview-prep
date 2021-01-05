import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].

def reverse_words(s) -> None:
    def reverse_range(s: list, start: int, end: int):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    reverse_range(s, 0, len(s) - 1)
    word_end = 0
    word_start = 0
    while word_end < len(s):
        if s[word_end] == ' ':
            if word_end > word_start:
                reverse_range(s, word_start, word_end - 1)
            word_end += 1
            word_start = word_end
        else:
            word_end += 1
    ## reverse the last word
    reverse_range(s, word_start, len(s) - 1)

        
def pythonic_reverse_words(s):
    return ' '.join(reversed(s.split(' ')))

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))
    # print(id(s_copy))
    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
