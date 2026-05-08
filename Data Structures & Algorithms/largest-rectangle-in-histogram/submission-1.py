class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heightStack = []
        startIndexStack = []
        maxArea = 0

        for index in range(len(heights)):
            # print(f"heights: {heightStack} startStack: {startIndexStack} maxArea: {maxArea} index: {index}")
            if len(heightStack) == 0 and len(startIndexStack) == 0:
                heightStack.append(heights[index])
                startIndexStack.append(index)
            elif heights[index] >= heightStack[-1]:
                # print(f"Found a higher height so adding to stack : {heights[index]}")
                heightStack.append(heights[index])
                startIndexStack.append(index)
            else:
                startIndex = 0
                while(heightStack and heightStack[-1] > heights[index]):
                    height = heightStack.pop()
                    startIndex = startIndexStack.pop()
                    area = height * (index-startIndex)
                    maxArea = max(maxArea, area)
                heightStack.append(heights[index])
                startIndexStack.append(startIndex)
        
        # print(f"heights: {heightStack} startStack: {startIndexStack} maxArea: {maxArea}")
        endIndex = len(heights)
        while len(heightStack) > 0:
            height = heightStack.pop()
            startIndex = startIndexStack.pop()
            area = height * (endIndex - startIndex)
            maxArea = max(maxArea, area)
        
        return maxArea


        