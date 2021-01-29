from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    number_arr = [
        ['0'],
        ['1'],
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I'],
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'Q', 'R', 'S'],
        ['T', 'U', 'V'],
        ['W', 'X', 'Y', 'Z'],
    ]
    if len(phone_number) == 0:
        return []
    if len(phone_number) == 1:
        return number_arr[int(phone_number[0])]
    return [
        character + remainder
        for remainder in phone_mnemonic(phone_number[1:])
            for character in number_arr[int(phone_number[0])]
    ]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
