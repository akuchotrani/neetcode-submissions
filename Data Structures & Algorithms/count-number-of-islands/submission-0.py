class Solution:

    def calculateNeighbours(self, row, col, grid, rows, cols):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        # print(f"Calculate Neighbours for {row} {col}")

        
        cell = str(row) + "," + str(col)

        if cell not in self.isVisited:
            self.isVisited.add(cell)
        else:
            return
        
        if grid[row][col] == "0":
            return
        
        self.calculateNeighbours(row-1, col, grid, rows, cols)
        self.calculateNeighbours(row, col-1, grid, rows, cols)
        self.calculateNeighbours(row+1, col, grid, rows, cols)
        self.calculateNeighbours(row, col+1, grid, rows, cols)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        isLandCounter = 0
        self.isVisited = set()
        for row in range(rows):
            for col in range(cols):
                cell = str(row) + ',' + str(col)
                if grid[row][col] == '1' and cell not in self.isVisited:
                    print(f"Island detected at : {row},{col}")
                    isLandCounter += 1
                    self.calculateNeighbours(row,col, grid, rows, cols)
        
        return isLandCounter


        

        