from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
            
        if k > len(nums):
            k = len(nums)

        dq = deque()
 
        for right in range(k):
            new_num = nums[right]
            if new_num in dq:
                return True
            dq.append(new_num)

        for i in range(k, len(nums)):
            new_num = nums[i]
            if new_num in dq:
                return True
            dq.popleft()
            dq.append(new_num)

        return False
        
