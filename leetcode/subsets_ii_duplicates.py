def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    def dfs(subset, next_unique):
        
        result.append(subset)

        for i in range(next_unique, len(unique_nums)):
            num = unique_nums[i]
            if counts[num] > 0:
                counts[num] -= 1
                dfs([*subset, num], i)
                counts[num] += 1
                
                
        
    counts = Counter(nums)
    unique_nums = list(counts.keys())
    result = []
    dfs([], 0)
    return result

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    def dfs(subset, start_from):
        
        result.append(subset)

        for i in range(start_from, len(nums)):
            if i > start_from and nums[i] == nums[i-1]:
                continue
            dfs([*subset, nums[i]], i + 1)
                
                
    nums.sort()
    result = []
    dfs([],0)
    return result