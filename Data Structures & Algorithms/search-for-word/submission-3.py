class Solution:

    def findWord(self, word, row, col, board):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False
        
        if word[0] == board[row][col]:
            remainingWord = word[1:]
            # print(f"found char: {word[0]} at r:{row} c:{col} remainingWord: {remainingWord}")
            if len(remainingWord) == 0:
                # print("Found the answer!!")
                return True
            board[row][col] = "#"
            found = (self.findWord(remainingWord, row-1, col, board)
                or self.findWord(remainingWord, row+1, col, board)
                or self.findWord(remainingWord, row, col-1, board)
                or self.findWord(remainingWord, row, col+1, board))
            board[row][col] = word[0]
            return found
        return False




    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                result = self.findWord(word, row, col, board)
                if result:
                    return result
        
        return False
        