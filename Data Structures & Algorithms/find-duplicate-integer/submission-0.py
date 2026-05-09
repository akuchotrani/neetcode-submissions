class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        
        slow_start = 0
        while True:
            slow_start = nums[slow_start]
            slow = nums[slow]
            if slow_start == slow:
                break
        
        return slow
            
        
        