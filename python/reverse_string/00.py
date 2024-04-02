class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            buff = s[right]            
            s[right] = s[left]
            s[left] = buff
            
            left += 1
            right -= 1

