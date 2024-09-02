import heapq
import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        if len(piles) == 0:
            return 0

        piles_alt = [-p for p in piles]
        heapq.heapify(piles_alt)

        for i in range(k):
            
            top_element = heapq.heappop(piles_alt)
            heapq.heappush(piles_alt, math.floor(top_element // 2))

            
        return abs(sum(piles_alt))
    
            
        
