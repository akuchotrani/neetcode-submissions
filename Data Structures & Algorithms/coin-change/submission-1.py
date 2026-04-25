class Solution:

    def dfs(self, coins, amountRemaining):
        if amountRemaining == 0:
            return 0

        if amountRemaining < 0:
            return float('inf')

        if amountRemaining in self.memo:
            return self.memo[amountRemaining]
        
        min_coin = float('inf')
        for coin in coins:
            res = self.dfs(coins, amountRemaining-coin)
            if res != float('inf'):
                min_coin = min(min_coin, res+1)
        self.memo[amountRemaining] = min_coin
        return min_coin

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        result = self.dfs(coins, amount)
        if result == float('inf'):
            return -1
        return result

        