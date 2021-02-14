from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_freq = Counter(p)
        start = end = 0
        char_freq = Counter()
        result = []
        
        while end < len(s):
            char = s[end]
            char_freq[char] += 1
            while (start <= end and 
                char_freq[char] > target_freq[char]):
                char_freq[s[start]] -= 1
                start += 1
            if end - start + 1 == len(p):
                result.append(start)
                char_freq[s[start]] -= 1
                start += 1
            end += 1
            
        return result