import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}

        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
        
        freq = [[] for _ in range(len(nums)+1)]
        for key, val in myDict.items():
            freq[val].append(key)
        
        print(freq)
        answer = []
        for i in range(len(nums), -1, -1):
            answer += freq[i]
            if len(answer) == k:
                break
        
        return answer
