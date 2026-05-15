class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(currIdx):
            if currIdx >= len(cost):
                return 0
            
            if currIdx in memo:
                return memo[currIdx]
            
            one_step = dfs(currIdx+1)
            two_step = dfs(currIdx+2)

            memo[currIdx] = cost[currIdx] + min(one_step, two_step)
            return memo[currIdx]
        
        self.memo = {}
        return min(dfs(0), dfs(1))