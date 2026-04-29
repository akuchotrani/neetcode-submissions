class Solution:

    def dfs(self, row, col, text1, text2):
        print(f"dfs called row: {row} col: {col}")
        if row < 0 or row >= len(text1) or col < 0 or col >= len(text2):
            print("Out of bounds")
            return 0
        
        if self.dp[row][col] != None:
            return self.dp[row][col]
        
        result = 0
        if text1[row] == text2[col]:
            res_diagonal = self.dfs(row+1, col+1, text1, text2) + 1
            print(f"res_diagonal: {res_diagonal}")
            result = res_diagonal
        else:
            res_down = self.dfs(row+1, col, text1, text2)
            res_right = self.dfs(row, col+1, text1, text2)
            print(f"row: {row} col: {col} res_down: {res_down} res_right: {res_right}")
            result = max(res_down, res_right)
                
        self.dp[row][col] = result
        return result
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp = [[None for _ in range(len(text2))] for _ in range(len(text1))]
        print(self.dp)
        self.dfs(0, 0, text1, text2)
        return self.dp[0][0]