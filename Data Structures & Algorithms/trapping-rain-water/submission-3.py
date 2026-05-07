# [0,2,2,3,3,3,3,3,3,3]
# [3,3,3,3,3,3,3,3,2,1]
# [0,2,2,3,3,3,3,3,2,1]
# [0,0,2,0,2,3,2,0,0,0]



class Solution:
    def trap(self, height: List[int]) -> int:
        leftShadow = []
        prev = 0
        for i in range(len(height)):
            prev = max(prev, height[i])
            leftShadow.append(prev)
        #print(f"{leftShadow}")
        rightShadow = [0 for _ in range(len(height))]
        nxt = 0
        for i in range(len(height)-1, -1, -1):
            nxt = max(nxt, height[i])
            rightShadow[i] = nxt
        #print(f"{rightShadow}")
        masked = []
        for i in range(len(height)):
            mask = min(leftShadow[i], rightShadow[i])
            masked.append(mask)
        
        #print(f"{masked}")
        result = 0
        for i in range(len(height)):
            diff = masked[i] - height[i]
            result += diff
        
        return result

        