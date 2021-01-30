
def longestPalindrome(s: str) -> str:
    def expandPalindrome(start, end):
        while start > 0 and end < len(s) - 1:
            if s[start - 1] == s[end + 1]:
                # print(s)
                # print(start - 1, s[start - 1], end + 1, s[end + 1])

                # print('yello')
                start -= 1
                end += 1
            else:
                break
        # print(start, end)

        return (start, end)

        
    max_palindrome = ''
    for i in range(len(s)):
        start, end = expandPalindrome(i, i)
        if i + 1 < len(s) and s[i] == s[i + 1]:
            start_even, end_even = expandPalindrome(i, i + 1)
            if (end_even - start_even) > (end - start):
                start, end = start_even, end_even
        
        if (end - start + 1) > len(max_palindrome):
            max_palindrome = s[start:(end+1)]


    return max_palindrome


if __name__ == '__main__':
    print('yolo')
    print('ANSWER', longestPalindrome('cbbd'))
    print('ANSWER', longestPalindrome('ccccbccc'))
    print('ANSWER', longestPalindrome('abcd'))
    print('ANSWER', longestPalindrome('ccc'))
    print('ANSWER', longestPalindrome('aaaa'))
    print('ANSWER', longestPalindrome('babad'))
    print('ANSWER', longestPalindrome('adam'))
    print('ANSWER', longestPalindrome('xaabacxcabaaxcabaax'))