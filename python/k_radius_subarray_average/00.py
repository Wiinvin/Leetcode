class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        if k == 0:
            return nums
        
        prefix = [0] * (len(nums)+1)
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            prefix[i+1] = acc
            
        sums = [-1] * len(nums)
        for i in range(len(nums)):
            if not (i-k < 0 or i+k > (len(nums)-1)):
                sums[i] = (prefix[i+k+1] - prefix[i-k]) // (2*k+1)
                
        return sums
    
