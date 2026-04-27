class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top = 0
        bottom = len(matrix)-1

        while top < bottom:
            for col in range(len(matrix[0])):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1
        #print(f"{matrix}")

        first = 0
        second = 0
        for first in range(len(matrix)):
            for second in range(first+1, len(matrix)):
                temp = matrix[second][first]
                matrix[second][first] = matrix[first][second]
                matrix[first][second] = temp
        
        # print("#############")
        #print(f"{matrix}")
        