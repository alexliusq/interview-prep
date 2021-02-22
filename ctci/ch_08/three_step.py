
from functools import cache

## this is unique COMBINATIONS of steps not unique PATHS which is permutations

# def three_step_memoized(n):
#     @cache
#     def helper(start, target):
#         if target < 0:
#             return 0
#         if target == 0:
#             return 1
        
#         count = 0
#         for i in range(start, len(steps)):
#             count += helper(i, target - steps[i])
        
#         return count
        
#     steps = [1,2,3]
#     count = helper(0, n)
#     return count

# def three_step_dynamic(n):
        
#     steps = [1,2,3]
#     result = [[1] + [0] * n for _ in range(len(steps))]
#     # print([id(l) for l in result])
#     for i, step in enumerate(steps):
#         for j in range(1, n + 1):
#             count = 0
#             if i > 0:
#                 count += result[i - 1][j]
#             if j >= step:
#                 count += result[i][j - step]
            
#             result[i][j] = count
#     # print(result)
#     return result[-1][-1]

@cache
def three_step_memoized(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return three_step_memoized(n - 1) + three_step_memoized(n - 2) + three_step_memoized(n - 3)

def three_step_dynamic(n):

    steps = [1,2,3]
    result = [1] + [0] * n

    for i in range(1, n + 1):
        for step in steps:
            if i - step >= 0:
                result[i] += result[i - step]
    
    return result[-1]

print(three_step_memoized(10))
print(three_step_dynamic(10))