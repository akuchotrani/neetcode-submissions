class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        runningProd = []
        prevMax = float('-inf')
        prevMin = float('inf')
        result = 0
        for i in range(len(nums)):
            if i == 0:
                result = nums[i]
                prevMax = max(nums[i], prevMax)
                prevMin = min(nums[i], prevMin)
            else:
                tempMax = max(nums[i], prevMax*nums[i], prevMin*nums[i])
                tempMin = min(nums[i], prevMax*nums[i], prevMin*nums[i])
                prevMax = tempMax
                prevMin = tempMin
                result = max(result, prevMax)
        return result
                


        