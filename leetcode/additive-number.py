
## 112358
## 1 - 1, 12, 123, 1235, 12358
## 11, 2, 23, 23

## Optimization: 9 + 99 = 108. len first + len second <= len third + 1


## 112358
## 1 - 1, 12, 123, 1235, 12358
## 11, 2, 23, 23

## Optimization: 9 + 99 = 108. len first + len second <= len third + 1

from typing import List
from functools import reduce

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def num_from_digits(digits: List[int]) -> int:
            return reduce(
                lambda x, y: x * 10 + y, digits
            )
        
        def has_leading_zero(digits: List[int]) -> bool:
            num_str = ''.join(str(x) for x in digits)
            return len(str(int(num_str))) != len(num_str)
            
        def first_pass() -> bool:
            # print('digits', digits)
            n = len(digits)
            for i in range(1, n):
                for j in range(i + 1, n):
                    if has_leading_zero(digits[:i]) or has_leading_zero(digits[i:j]):
                        continue
                    first = num_from_digits(digits[:i])
                    second = num_from_digits(digits[i:j])
                    if remainder(first, second, j):
                        return True
            return False
        
        def remainder(first: int, second: int, idx: int) -> bool:
            if idx == len(digits):
                return True

            expected = first + second
            next_idx = idx + len(str(expected))

            if next_idx > len(digits):
                return False
            if has_leading_zero(digits[idx:next_idx]):
                return False
            third = num_from_digits(digits[idx:next_idx])
            if third == expected:
                return remainder(second, third, next_idx)
            return False
        
        
        if len(num) < 3:
            return False
        digits = [int(x) for x in num]
        return first_pass()

test = Solution()
assert test.isAdditiveNumber('101') == False
assert test.isAdditiveNumber('199100199') == True
assert test.isAdditiveNumber('19910019') == False
assert test.isAdditiveNumber('112358') == True
