class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        curr = 0
        minlen = float('inf')
        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                minlen = min(minlen, right-left+1)
                curr -= nums[left]
                left += 1

        return minlen if left else 0
