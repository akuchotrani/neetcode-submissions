class Solution:
    def dfs(self, nums, curr, pos):
        # print(f"answer: {self.answer} curr: {curr} pos: {pos}")
        
        self.answer.append(curr)
        for i in range(pos, len(nums)):
            curr.append(nums[i])
            self.dfs(nums, curr.copy(), i+1)
            curr.pop()

        

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.dfs(nums, [], 0)
        return self.answer