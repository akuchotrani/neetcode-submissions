class Solution:

    def checkBoardValid(self, board, row, col):
        # print(f"Checkboardvalid called for : {row},{col} board: {board}")
        if row < 0 or col < 0 or row >= len(board) or col >= len(board):
            return False
        
        totalRow = len(board)
        for i in range(totalRow):
            if board[i][col] == 'Q' and (i != row):
                # print("-- Same row collision")
                return False
        
        totalCol = len(board)
        for i in range(totalCol):
            if board[row][i] == 'Q' and (i!=col):
                # print("-- Same col collision")
                return False
        
        # all 4 diagonal directions
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < totalRow and 0 <= c < totalCol:
                if board[r][c] == 'Q':
                    return False
                r += dr
                c += dc

        return True


    def dfs(self, board, n, row, col):
        if n == 0:
            self.result.append(["".join(r) for r in board])
            return
        
        if row < 0 or col < 0 or row >= len(board) or col >= len(board):
            return
        
        totalCol = len(board)
        for i in range(totalCol):
            print(f"Placing Queen at {row},{i}")
            board[row][i] = 'Q'
            if self.checkBoardValid(board, row, i):
                self.dfs(board, n-1, row+1, 0)
            board[row][i] = '.'
        

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        self.result = []
        for i in range(n):
            board.append([])
            for j in range(n):
                board[i].append('.')
        # print(board)
        self.dfs(board, n, 0, 0)
        return self.result