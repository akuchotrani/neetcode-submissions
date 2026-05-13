class Solution:

    def dfs(self, n):
        # print(f"DFS called for {n}")
        if n == 1:
            return True
        
        if n in self.memo:
            return False
        self.memo[n] = True
        total = 0
        while n:
            unitDigit = n%10
            n = n//10
            total += pow(unitDigit, 2)
        return self.dfs(total)

    def isHappy(self, n: int) -> bool:
        self.memo = {}
        return self.dfs(n)