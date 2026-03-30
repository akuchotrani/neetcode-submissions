class Solution:
    def check_sub_box(self, row, col, board):
        myDict = {}
        for i in range(row, row+3, 1):
            for j in range(col, col+3, 1):
                if board[i][j] != "." and board[i][j] in myDict:
                    print(f"Failed at check_sub_box at {i},{j} value duplicated {board[i][j]}")
                    return False
                else:
                    myDict[board[i][j]] = 1
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if row%3 == 0 and col%3 == 0:
                    result = self.check_sub_box(row, col, board)
                    if result == False:
                        return False

        for row in range(len(board)):
            rowDict = {}
            for col in range(len(board[0])):
                if board[row][col] != "." and board[row][col] in rowDict:
                    return False
                else:
                    rowDict[board[row][col]] = 1
        
        for col in range(len(board[0])):
            colDict = {}
            for row in range(len(board)):
                if board[row][col] != "." and board[row][col] in colDict:
                    return False
                else:
                    colDict[board[row][col]] = 1
        
        return True

        