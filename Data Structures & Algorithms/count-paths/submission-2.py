class Solution:
    def findPath(self, currRow, currCol, m, n):
        # print(f"findPath row: {currRow} col: {currCol}")
        if currRow == m-1 and currCol == n-1:
            return 1
        if currRow < 0 or currRow >= m or currCol < 0 or currCol>= n:
            return -1
        
        if self.cache[currRow][currCol] != None:
            return self.cache[currRow][currCol]
        
        res_down = self.findPath(currRow+1, currCol, m, n)
        res_right = self.findPath(currRow, currCol + 1, m, n)
        # print(f"res_down: {res_down} res_right: {res_right}")
        if res_down != -1 and res_right != -1:
            self.cache[currRow][currCol] = res_down + res_right
        elif res_down == -1:
            self.cache[currRow][currCol] = res_right
        else:
            self.cache[currRow][currCol] = res_down
        return self.cache[currRow][currCol]

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        self.cache = [[None for _ in range(n)] for _ in range(m)]
        self.cache[m-1][n-1] = 0
        print(self.cache)
        self.findPath(0, 0, m, n)
        print(self.cache)
        return self.cache[0][0]