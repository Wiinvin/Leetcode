from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.que = deque()        
        self.size = size
    def next(self, val: int) -> float:
        self.que.append(val)
        if len(self.que) > self.size:
            self.que.popleft()
        return sum(self.que) / len(self.que)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
