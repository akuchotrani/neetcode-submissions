class Solution:

    def binarySearch(self, nums, target, first, second):

        while first <= second:
            mid = (first+second)//2
            if nums[mid] == target:
                return nums[mid]
            
            if nums[mid] > target:
                second = mid - 1
            else:
                first = mid + 1

        return -1


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        unique = set()
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums)-2):
            first = nums[i]
            for j in range(i+1, len(nums)-1):
                second = nums[j]
                remaining = -1*(first+second)
                third = self.binarySearch(nums, remaining, j+1, len(nums)-1)
                if third != -1:
                    if (first,second,third) not in unique:
                        result.append([first, second, third])
                        unique.add((first, second, third))

        return result

        

        