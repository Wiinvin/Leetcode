class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cum = [nums[0]]
        for i in range(1, len(nums)):
            cum.append(cum[i-1] + nums[i])
        
        min_val = min(cum)
        if min_val > 0:
            return 1
        else:
            return -1 * min_val + 1
