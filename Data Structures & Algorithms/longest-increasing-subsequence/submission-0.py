class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.dp = {}
        for i in range(len(nums)):
            self.dp[i] = 0
        
        self.dp[len(nums)-1] = 1
        i = len(nums) - 2
        while i >= 0:
            for j in range(i, len(nums)):
                temp = 0
                if nums[i] < nums[j]:
                    temp = self.dp[j]
                self.dp[i] = max(1, self.dp[i], temp+1)
            i = i-1
        # print(self.dp)
        return max(self.dp.values())


        