

class Solution:
    def dfs(self, index, nums):
        if index >= len(nums):
            return 0
        if index in self.memo:
            return self.memo[index]
        res = max(nums[index] + self.dfs(index+2, nums), self.dfs(index+1, nums))
        self.memo[index] = res
        return res

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        first_copy = nums[:-1]
        second_copy = nums[1:]

        print(f"first: {first_copy} second: {second_copy}")
        self.memo = {}
        res_1 = self.dfs(0, first_copy)
        self.memo = {}
        res_2 = self.dfs(0, second_copy)
        return max(res_1, res_2)
        