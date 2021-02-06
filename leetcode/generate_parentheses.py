from typing import List

# def generateParenthesis(n: int) -> List[str]:
#     def next_set(left, right, n):
#         print(n)
#         if n <= 0:
#             result.add(left + right)
#             return
        
#         next_set('()' + left, right, n - 1)
#         next_set('(' + left + ')', right, n - 1)
#         next_set(left + '(', ')' + right, n - 1)
#         next_set(left, '(' + right + ')', n - 1)
#         next_set(left, right + '()', n - 1)
#         next_set('(' + left, right + ')', n - 1)
        
#     result = set()
#     next_set('', '', n)
#     return list(result)

def generateParenthesis(self, n: int) -> List[str]:
    def backtrack(parens, left, right):
        if left == n and right == n:
            result.append(parens)
            return
        
        if left < n:
            backtrack(parens + '(', left + 1, right)
        if right < left:
            backtrack(parens + ')', left, right + 1)
    
    result = []
    backtrack('', 0, 0)
    return result
    

print(generateParenthesis(4))