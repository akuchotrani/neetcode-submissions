class Solution:
    def dfs(self, i, s):
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0
        if i in self.memo:
            return self.memo[i]
            
        res = self.dfs(i+1, s)
        if i + 1 < len(s):
            if s[i] == '1' or (s[i] == "2" and s[i+1] < '7'):
                res += self.dfs(i+2, s)
        self.memo[i] = res
        return res

    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.dfs(0, s)
        
        