class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ## 65 to 90
        ans = 0
        strlen = len(columnTitle)
        multiplier = 26 ** strlen
        for ch in columnTitle:
            ans += (ord(ch) - 64) * multiplier / 26
            multiplier /= 26
        return int(ans)
