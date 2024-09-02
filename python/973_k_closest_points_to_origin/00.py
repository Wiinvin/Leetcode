import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        if k == len(points):
            return points
        
        heap = []        
        for i in range(len(points)):
            heapq.heappush(heap, (-1 * (points[i][0] ** 2 + points[i][1] ** 2), i))
            
            if len(heap) > k:
                heapq.heappop(heap)
                #print(heap)
                

        return [points[ele[1]] for ele in heap]

