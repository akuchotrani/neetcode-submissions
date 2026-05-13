class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        count = len(nums)
        for i in range(count):
            nums.append(nums[i])
        return nums
        