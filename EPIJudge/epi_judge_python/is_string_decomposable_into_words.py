import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    @functools.cache
    def prefix_to_words(chars_before) -> List[str]:
        for index in range(chars_before):
            word = ''.join(domain[index:chars_before])
            if word in dictionary:
                if index == 0:
                    return [word]

                prev_words = prefix_to_words(index)
                # print(word, prev_prefix)
                if prev_words:
                    new_words = prev_words[:] + [word]
                    return new_words
        return []

    result = prefix_to_words(len(domain))
    print(result)
    return result


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
