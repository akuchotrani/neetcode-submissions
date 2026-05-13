class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        myHeap = []
        for point in points:
            distance = pow(point[0], 2) + pow(point[1],2)
            if len(myHeap) < k:
                # print(f"Less element in heap so pushing : {point}")
                heapq.heappush(myHeap, (-1*distance, point))
            else:
                top = myHeap[0]
                if top[0]*-1 > distance:
                    heapq.heappop(myHeap)
                    heapq.heappush(myHeap, (-1*distance, point))
        # print(f"Final heap: {myHeap}")
        answer = []
        for item in myHeap:
            answer.append(item[1])
        return answer

        