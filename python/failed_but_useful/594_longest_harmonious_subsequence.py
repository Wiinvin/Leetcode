class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0

        if len(nums) < 2:
            return ans

        left = 0
        for i in range(left, len(nums)):
            if ans > len(nums) - left:
                break
            right = len(nums) - 1
            diff = 0
            ## this right pointer loop
            #
            while right > left: 
                if diff == 1:
                    ## clean up the array by removing high values
                    #
                    subseq = nums[i:right + 1]
                    print(subseq)
                    j = 1
                    while j < len(subseq):
                        if abs(subseq[j] - subseq[0]) > 1:
                            subseq.pop(j)
                        j += 1
                    ans = max(ans, len(subseq))
                    break
                diff = abs(nums[i] - nums[right])
                right -= 1

            left += 1
        return ans

