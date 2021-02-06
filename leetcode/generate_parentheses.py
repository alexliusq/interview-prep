from typing import List

def generateParenthesis(n: int) -> List[str]:
    def next_set(left, right, n):
        print(n)
        if n <= 0:
            result.add(left + right)
            return
        
        next_set('()' + left, right, n - 1)
        next_set('(' + left + ')', right, n - 1)
        next_set(left + '(', ')' + right, n - 1)
        next_set(left, '(' + right + ')', n - 1)
        next_set(left, right + '()', n - 1)
            
        
    result = set()
    next_set('', '', n)
    return list(result)
    

print(generateParenthesis(4))