from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(magazine) < len(ransomNote) or magazine == '':
            return False
        if ransomNote == '':
            return True
        
        odict = defaultdict(int)
        rset = set()
        for i,c in enumerate(magazine):
            if i < len(ransomNote):
                odict[ransomNote[i]] += 1
                rset.add(ransomNote[i])
            odict[c] -= 1
        
        for c in rset:
            if odict[c] > 0:
                return False
            
        return True
