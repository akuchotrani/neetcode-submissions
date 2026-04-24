class Solution:
    def dfs(self, index, nums):
        if index >= len(nums):
            return 0
        if index in self.memo:
            return self.memo[index]
        
        res = max(nums[index] + self.dfs(index + 2, nums), self.dfs(index+1, nums))
        self.memo[index] = res
        return res

    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.dfs(0, nums)
        