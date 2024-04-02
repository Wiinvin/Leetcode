class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        curr = 0
        result = 0
        for i in range(k):
            result += nums[i]
        curr = result
        for right in range(k, len(nums)):
            curr -= nums[left]
            curr += nums[right]
            result = max(result, curr)
            left += 1
        return result/k
    
