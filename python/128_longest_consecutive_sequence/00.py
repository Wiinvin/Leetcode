
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return len(nums)

        el_cntr = set(nums)
        ans = 1
        i = 0
        ks = sorted(list(el_cntr))

        while i < len(ks)-1:
            seqlen = 1
            while i < len(ks)-1 and ks[i] + 1 == ks[i+1]:
                seqlen += 1
                i += 1
            ans = max(ans, seqlen)
            i += 1

        return ans
