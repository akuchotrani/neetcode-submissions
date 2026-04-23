class Solution:

    def climb(self, n):
        if n in self.memo:
            return self.memo[n]
    
        if n < 0:
            return 0
        
        if n == 0:
            return 1
        res_1 = self.climb(n-1)
        if res_1 != 0:
            self.memo[n-1] = res_1
        
        res_2 = self.climb(n-2)
        if res_2 != 0:
            self.memo[n-2] = res_2
        
        return self.climb(n-1) + self.climb(n-2)

    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.climb(n)

        