class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left = 0 
        right = 1

        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return [nums[0]**2]
        
        ## find indices of minimum value
        #
        while abs(nums[right]) <= abs(nums[left]) :
            left += 1
            right += 1
            if right == len(nums):
                break
                
            
        min_idx = left
        ans = [nums[min_idx]**2]
        
        i = min_idx
        j = min_idx
        
        while len(ans) != len(nums):
            
            if i == 0:
                while j < len(nums) - 1:
                    j += 1
                    ans.append(nums[j]**2)
                    
            elif j == len(nums) - 1:
                while i > 0:
                    i -= 1
                    ans.append(nums[i]**2)
              
            elif abs(nums[i - 1]) <= abs(nums[j + 1]):
                ans.append(nums[i-1]**2)
                i -= 1
                
            elif abs(nums[j + 1]) < abs(nums[i - 1]):
                ans.append(nums[j+1]**2)
                j += 1        
        
        
        return ans
        
