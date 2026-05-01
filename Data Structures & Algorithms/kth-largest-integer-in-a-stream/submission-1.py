class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.myHeap = []
        self.k = k
        for val in nums:
            self.add(val)
        

    def add(self, val: int) -> int:
        if len(self.myHeap) < self.k:
            heapq.heappush(self.myHeap, val)
        else:
            if self.myHeap[0] < val:
                heapq.heappop(self.myHeap)
                heapq.heappush(self.myHeap, val)
        return self.myHeap[0]
        
