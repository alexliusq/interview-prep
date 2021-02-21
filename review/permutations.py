from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    def helper(start):
        if start == len(nums):
            result.append[nums.copy()]
            
        for i in range(start, len(nums)):
            A[start], A[i] = A[i], A[start]
            helper(start + 1)
            A[i], A[start] = A[start], A[i]
    
    result = []
    helper(0)
    return result

permute(list(range(5)))