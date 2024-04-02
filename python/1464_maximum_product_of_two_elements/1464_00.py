class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            return (nums[0] - 1) * (nums[1] - 1)
        stack = [nums[0]]

        for i in range(1,len(nums)):
            if nums[i] > stack[-1]:
                tmp = []

                while stack and nums[i] > stack[-1]:
                    
                    tmp.append(stack.pop())
                    
                stack.append(nums[i])
                for j in range(len(tmp)):
                    stack.append(tmp.pop())
            else:
                stack.append(nums[i])
        
        return (stack[0] - 1) * (stack[1] - 1)
