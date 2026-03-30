class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[left]
        while left < right:
            mid = (left+right) // 2
            print(f"left: {left} right: {right} mid:{mid}")
            if nums[left] <= nums[right]:
                result = nums[left]
                return result
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

            
        