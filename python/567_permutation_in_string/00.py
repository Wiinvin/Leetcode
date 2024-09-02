from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        if len(s1) == len(s2):
            return True if Counter(s1) == Counter(s2) else False
        
        s1_list = [c for c in s1]
        s1_dict = Counter(s1_list)

        left = 0
        for right in range(len(s1)-1, len(s2)):
            tgt_substr = s2[left: right+1]
            tgt_substr_list = [c for c in tgt_substr]
            s2_subset_dict = Counter(tgt_substr)
            if s2_subset_dict == s1_dict:
                return True
            left += 1

        return False

