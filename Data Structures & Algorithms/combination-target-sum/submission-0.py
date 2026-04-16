class Solution:

    def recursiveSum(self, nums, remaining_target, choices, start):
        # print(f"Recursive Sum: {remaining_target} choices:{choices}")
        if remaining_target == 0:
            self.answer.append(choices[:])
        
        if remaining_target < 0:
            return
        
        for i in range(start, len(nums)):
            choices.append(nums[i])
            self.recursiveSum(nums,remaining_target - nums[i], choices, i)
            choices.pop()                

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.answer = []
        choice = []
        self.recursiveSum(nums, target, choice, 0)
        return self.answer

        