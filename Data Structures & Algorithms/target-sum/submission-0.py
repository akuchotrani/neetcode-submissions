class Solution:
    def dfs(self, nums, index, currTotal, target):
        if index == len(nums):
            if currTotal == target:
                self.answer += 1
            return
        
        self.dfs(nums, index+1, currTotal+nums[index], target)
        self.dfs(nums, index+1, currTotal-nums[index], target)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.answer = 0
        self.dfs(nums, 0, 0, target)
        return self.answer
        