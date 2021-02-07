from typing import List

# def permute(nums: List[int]) -> List[List[int]]:
#     def backtrack(start_from):
#         if start_from == len(nums):
#             result.append([*nums])
#             return
        
#         for i in range(start_from, len(nums)):
#             nums[start_from], nums[i] = nums[i], nums[start_from]
#             backtrack(start_from + 1)
#             nums[start_from], nums[i] = nums[i], nums[start_from]
    
#     result = []
#     backtrack(0)
#     return result

def permute(nums: List[int]) -> List[List[int]]:
    def dfs(remainder, current):
        if not remainder:
            result.append(current)
            return
        
        for i, num in enumerate(remainder):
            dfs(remainder[:i] + remainder[(i+1):], [*current, num])
        
        
    result = []
    dfs(nums, [])
    return result

permute([1,2,3])