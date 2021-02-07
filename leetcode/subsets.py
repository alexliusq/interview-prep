def subsets(self, nums: List[int]) -> List[List[int]]:
    def backtrack(subset, num_count):
        if num_count == len(nums):
            result.append(subset)
            return
        
        num = nums[num_count]
        backtrack([*subset, num], num_count + 1)
        backtrack(subset, num_count + 1)
        
    result = []
    backtrack([], 0)
    return result

def subsets(self, nums: List[int]) -> List[List[int]]:
    def dfs(subset, start_from):
        
        result.append(subset)
        
        for i in range(start_from, len(nums)):
            num = nums[i]
            dfs([*subset, num], i + 1)
        
    result = []
    dfs([], 0)
    return result