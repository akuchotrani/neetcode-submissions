class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1

        # Find the row from top to bottom using binary search
        top = 0
        bottom = rows
        while(top <= bottom):
            mid = (top+bottom)//2
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                top = mid + 1
            else:
                bottom = mid - 1
        
        # binary search in cols
        left = 0
        right = cols
        while(left <= right):
            mid = (right+left)//2
            if target == matrix[top-1][mid]:
                return True
            elif target > matrix[top-1][mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

        