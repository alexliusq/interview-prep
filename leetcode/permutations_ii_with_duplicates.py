from typing import List

def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    def directed_permute(to_select):
        if to_select == len(nums):
            result.append([*nums])
            return
        
        swapped = set()
        for i in range(to_select, len(nums)):
            if nums[i] not in swapped:
                swapped.add(nums[i])
                nums[i], nums[to_select] = nums[to_select], nums[i]
                directed_permute(to_select + 1)
                nums[i], nums[to_select] = nums[to_select], nums[i]
    
    result = []
    directed_permute(0)
    return result