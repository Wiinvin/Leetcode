class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k or k == 0:
            return 0
        
        
        vowels = ["a", "e", "i", "o", "u"]
        prev = 0
        j = 0
        right = k
        while j < right:
            if s[j] in vowels:
                prev += 1
            j += 1
 
        left = 0
        maxlen = prev
        curr = prev
        while right < len(s):
            if s[right] in vowels:
                curr += 1
     
            if s[left] in vowels:
                curr -= 1

            maxlen = max(maxlen, curr)
            prev = curr

            right += 1
            left += 1

        return maxlen

