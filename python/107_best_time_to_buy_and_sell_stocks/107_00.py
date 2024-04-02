class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = ans = 0
        low = prices[0]
        for right in range(len(prices)):

            if prices[right] - prices[left] < 0:
                low = min(low, prices[right])
                left = right
            ans = max(ans, prices[right] - prices[left])
            
        return ans

