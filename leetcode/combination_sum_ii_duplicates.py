def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    def dfs(candidates, combo, target):
        if target == 0:
            result.append(combo)
            return
        if target < 0:
            return
        
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            candidate = candidates[i]
            dfs(candidates[i+1:], [*combo, candidate], target - candidate)
    
    result = []
    candidates.sort()
    dfs(candidates, [], target)
    return result