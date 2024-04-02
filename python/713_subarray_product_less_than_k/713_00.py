class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            return 0
        
        ans = 1
        n = 0
        left = 0
        for right in range(len(nums)):
            ans *= nums[right]
            
            while ans >= k:
                ans //= nums[left]
                left += 1
            
            n += right - left + 1
        return n
