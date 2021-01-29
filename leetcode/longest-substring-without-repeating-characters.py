from collections import OrderedDict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = OrderedDict()
        max_length = 0
        for char in s:
            if char in substring:
                popped = ''
                while popped != char:
                    popped, _ = substring.popitem(False)
                
            substring[char] = True
            
            substring_length = len(substring)
            if substring_length > max_length:
                max_length = substring_length
        
        return max_length