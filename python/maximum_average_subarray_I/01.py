class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        curr = 0
        right = 0
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

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums) == 1:
            return nums[0]
        if k > len(nums):
            return None
        
        curr = 0
        running_sum = sum(nums[:k])
        ans = running_sum / float(k)
        
        for i in range(k, len(nums)):
            curr = running_sum - nums[i-k] + nums[i]
            ans = max(ans, curr/float(k))
            running_sum = curr
            
        return ans
