from typing import List

NUM_TO_LETTERS = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

## O(3 ^ n) solution. faster than most leetcoders probably because i use indexing
## two basecases somewhat inelegant but it's fine
def letterCombinations(digits: str) -> List[str]:
    def combinationsHelper(index):
        if index >= len(digits):
            return []

        next_combos = combinationsHelper(index + 1)
        letters = NUM_TO_LETTERS[int(digits[index])]
        if not next_combos:
            return [[letter] for letter in letters]
        
        result = []
        for letter in letters:
            for combo in next_combos:
                result.append([letter, *combo])
        return result
    
    combos = combinationsHelper(0)
    return [''.join(combo) for combo in combos]
        



print(letterCombinations('23'))
print(letterCombinations(''))
print(letterCombinations('2'))
