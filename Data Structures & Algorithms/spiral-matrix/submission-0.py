class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        topPtr = 0
        bottomPtr = len(matrix) - 1
        leftPtr = 0
        rightPtr = len(matrix[0]) - 1
        result = []
        while topPtr <= bottomPtr and leftPtr <= rightPtr:
            for col in range(leftPtr, rightPtr + 1):
                result.append(matrix[topPtr][col])
            topPtr += 1
            for row in range(topPtr, bottomPtr + 1):
                result.append(matrix[row][rightPtr])
            rightPtr-= 1

            if topPtr <= bottomPtr:
                for col in range(rightPtr, leftPtr - 1, -1):
                    result.append(matrix[bottomPtr][col])
                bottomPtr-= 1

            if leftPtr <= rightPtr:
                for row in range(bottomPtr, topPtr - 1, -1):
                    result.append(matrix[row][leftPtr])
                leftPtr += 1

        return result
        