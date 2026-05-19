class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myHeap = []
        for num in nums:
            if len(myHeap) < k:
                heapq.heappush(myHeap, num)
            else:
                if myHeap[0] < num:
                    heapq.heappop(myHeap)
                    heapq.heappush(myHeap, num)
        # print(f"{myHeap}")
        return myHeap[0]
            
        