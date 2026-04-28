class Solution:
    def jump(self, nums, currIdx):
        print(f"currIdx: {currIdx}")
        if currIdx >= len(nums)-1:
            return True
        if currIdx in self.memo:
            return self.memo[currIdx]
        for jumpLength in range(nums[currIdx], 0, -1):
            res = self.jump(nums, currIdx + jumpLength)
            if res == True:
                self.memo[currIdx] = True
                return True
        self.memo[currIdx] = False
        return False

    def canJump(self, nums: List[int]) -> bool:
        self.memo = {}
        return self.jump(nums, 0)