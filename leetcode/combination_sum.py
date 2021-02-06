from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(combination, comb_sum, index):
        # print(combination, comb_sum, index)
        if comb_sum == target:
            result.append(combination)
            return
        if comb_sum > target or index >= len(candidates):
            return

        candidate = candidates[index]
        for multiple in range(target // candidate + 1):
            backtrack(combination + [candidate] * multiple, comb_sum + candidate * multiple, index + 1)
        
    
    result = []
    backtrack([], 0, 0)
    print(result)
    return result


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:

    def dynamic(candidate_index):
        # print(combination, comb_sum, index)
        candidate = candidates[candidate_index]
        for num in range(1, target + 1):
            if num >= candidate:
                result[candidate_index][num].extend([*combo, candidate] for combo in result[candidate_index][num - candidate])
            if candidate_index > 0:
                result[candidate_index][num].extend(result[candidate_index - 1][num])
            print(result)

        
    result = [[[] for _ in range(target + 1)] for _ in range(len(candidates))]
    # print(result)
    for i in range(len(candidates)):
        result[i][0] = [[]]
        dynamic(i)
    print(result[-1][-1])
    return result[-1][-1]


# combinationSum([2,3,6,7], 7)
combinationSum([2,3,5], 8)