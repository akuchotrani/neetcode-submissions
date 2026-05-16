class Solution:

    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0
        
        if grid[row][col] == 0:
            return 0
        
        if (row,col) in self.isVisited:
            return 0
        
        self.isVisited.add((row,col))
        
        
        return (1 + self.dfs(grid, row-1, col) + self.dfs(grid, row+1, col) + self.dfs(grid, row, col-1) + self.dfs(grid, row, col+1))
        

        
        


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.isVisited = set()
        max_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = self.dfs(grid, row, col)
                    # print(f"Area: {area} for row:{row} col: {col}")
                    max_area = max(max_area, area)
        
        return max_area
                    

        
        