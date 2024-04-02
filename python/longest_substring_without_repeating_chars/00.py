from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        if s == "":
            return maxlen
        
        subset = []
        left = right = 0
        while right < len(s):
            
            if s[right] in subset:
                maxlen = max(maxlen, right - left)
                while s[right] in subset:
                    subset.pop(0)
                    left += 1
                    
            subset.append(s[right])
            right += 1
        maxlen = max(maxlen, right - left)
        return maxlen
