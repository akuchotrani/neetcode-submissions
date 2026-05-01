import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowerBound = 1
        upperBound = max(piles)
        minK = float("inf")

        while lowerBound <= upperBound:
            k = ((upperBound+lowerBound) // 2)
            # print(f" low: {lowerBound} up:{upperBound} k:{k}")

            eatingHours = 0
            for i in range(len(piles)):
                eatingHours += math.ceil(piles[i]/k)
            
            if eatingHours <= h:
                minK = min(minK, k)
                upperBound = k - 1
            else:
                lowerBound = k + 1 
            #print(f"eatinghrs: {eatingHours} k: {k} minK:{minK}")
        return minK
            


        

        