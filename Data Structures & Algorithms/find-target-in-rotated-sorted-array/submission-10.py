class Solution:
    def binary_search(self, nums, target, left, right):
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        pivot = len(nums) - 1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        while(left < right):
            print(f"left: {left} right: {right} mid: {mid}")
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                pivot = mid
                print(f"Found a deflection point at {pivot}")
                break
            if mid > 0 and nums[mid - 1] > nums[mid]:
                pivot = mid - 1
                print(f"Found a deflection point at {pivot}")
                break
                
            if nums[left] <= nums[mid]:
                print("Forwarding left ptr")
                left = mid + 1
            else:
                print("Backing right ptr")
                right = mid - 1

        print(f"Final deflection point: {pivot}")

        result = -1
        print(f"{nums[0]} and {nums[pivot]}")
        if target >= nums[0] and target <= nums[pivot]:
            print(f"Searching left sub arrary :{0} to {pivot}")
            result = self.binary_search(nums, target, 0, pivot)
        else:
            print(f"Searching right sub arrary :{pivot+1} to {len(nums)-1}")
            result = self.binary_search(nums, target, pivot+1, len(nums)-1)

        return result
        