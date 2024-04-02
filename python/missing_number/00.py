class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        st = 0
        for i in range(len(nums)+1):
            if st not in nums:
                return st
            st += 1
    
