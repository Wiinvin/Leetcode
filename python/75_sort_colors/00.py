class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)  < 2:
            return nums

        for right in range(1, len(nums)):
            left = right - 1
            while left > -1 and nums[right] < nums[left]:
                left -= 1

            buf, nums[left+1] = nums[left+1], nums[right]

            for j in range(left+2, right+1):
                tmp = nums[j]
                nums[j] = buf
                buf = tmp



