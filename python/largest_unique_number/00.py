class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        odict = defaultdict(int)
        ans = -1
        for i in nums:
            odict[i] += 1
            
        for i,j in odict.items():
            if j == 1:
                ans = max(ans, i)
        
        return ans 

