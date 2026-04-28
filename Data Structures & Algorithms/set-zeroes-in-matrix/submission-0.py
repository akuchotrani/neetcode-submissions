class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row = set()
        zero_col = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_row.add(row)
                    zero_col.add(col)
        
        for row in range(len(matrix)):
            if row in zero_row:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0

        for col in range(len(matrix[0])):
            if col in zero_col:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
        


        
        