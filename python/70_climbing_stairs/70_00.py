class Solution:
    def climbStairs(self, n: int) -> int:

        def fibn(m: int) -> int:
            if m < 3: return m
            return fibn(m-1) + fibn(m-2)

        return fibn(n)
    
