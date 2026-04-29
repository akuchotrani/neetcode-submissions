class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningMaxSum = [nums[0]]
        for i in range (1,len(nums)):
            prev = runningMaxSum[i-1]
            temp = prev+nums[i]
            runningMaxSum.append(max(temp, nums[i]))
        # print(f"runningMaxSum: {runningMaxSum}")
        return max(runningMaxSum)


        