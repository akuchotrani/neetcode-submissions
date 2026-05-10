class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        myHeap = []
        for stone in stones:
            heapq.heappush(myHeap, -1*stone)
        
        while len(myHeap) > 1:
            stone1 = -1 * heapq.heappop(myHeap)
            stone2 = -1 * heapq.heappop(myHeap)
            # print(f"Stone1: {stone1} Stone2: {stone2}")
            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                heapq.heappush(myHeap, -1* (stone1-stone2))
            else:
                heapq.heappush(myHeap, -1 * (stone2-stone1))
        
        if len(myHeap) == 0:
            return 0
        
        return -1*myHeap[0]
        