def isprime(n):
        if n % 2 == 0 and n != 2:
            return False
        for i in range(3, int(n / 2)):
            if n % i == 0:
                return False
        return True
class Solution:

    

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        prime = 0
        numlen = len(nums)
        i = 0
        for _ in range(len(nums)):
            if isprime(nums[i][i]) and nums[i][i] > prime:
                prime = nums[i][i]
            if isprime(nums[i][numlen-i-1]) and nums[i][numlen-i-1] > prime:
                prime = nums[i][numlen-i-1]
            i += 1
    
        return prime
