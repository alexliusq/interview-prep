

# if temp = rev * 10 + pop, rev must be >= int_max / 10
# if rev == INTMAX / 10, then temp = rev * 1- + pop will overflow if and only if pop > 7
# Because 2^31-1 - 2,147,483,647 (last digit is 7 for positive limit)
# and 2^31=-2,147,483,648 (last digit is -8 for negative limit)

def reverse(self, x: int) -> int:
    result = 0
    max_num = 2 ** 31 - 1
    min_num = - 2 **31
    is_negative = False
    if x < 0:
        x = -x
        is_negative = True
    
    while x > 0:
        digit = x % 10
        result = result * 10 + digit
        ## leetcode java checking for overflow
        ## if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
        ## if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
        if result >= max_num or result <= min_num:
            return 0
        x //= 10
        
    return -result if is_negative else result
            