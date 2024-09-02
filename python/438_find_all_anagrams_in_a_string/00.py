from collections import defaultdict, Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(p) > len(s):
            return ans

        
        win_chars = defaultdict(int)
        left = 0
        for right in range(len(p)-1):
            win_chars[s[right]] += 1
        
        tgt_set = Counter(p)
        for right in range(len(p)-1, len(s)):
            win_chars[s[right]] += 1
            if win_chars == tgt_set:
                ans.append(left)
            win_chars[s[left]] -= 1
            if win_chars[s[left]] == 0:
                del win_chars[s[left]]
            
            left += 1

        return ans
