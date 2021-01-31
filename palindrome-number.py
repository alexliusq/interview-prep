
# def isPalindrome(x: int) -> bool:
#     return int(''.join(reversed(str(abs(x))))) == x

#121
# 12, 1
# 1, 12

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    reversed_num = 0
    original = x
    while x > 0:
        popped = x % 10
        reversed_num = reversed_num * 10 + popped
        x //= 10
    return original == reversed_num


if __name__ == '__main__':
    print(isPalindrome(10))
    print(isPalindrome(101))