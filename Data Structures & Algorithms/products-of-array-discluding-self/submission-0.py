# 1 2 4 6
# 1   1   2  8
# 48  24  6  1


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [ 1 for _ in range(len(nums))]
        rightProduct = [ 1 for _ in range(len(nums))]

        answer = []

        left = 1
        prev = 1
        for i in range(len(nums)):
            prod = left*prev
            leftProduct[i] = prod
            prev = nums[i]
            left = prod
        
        right = 1
        prev = 1
        for j in range(len(nums)-1, -1, -1):
            #print(f"prev: {prev} right: {right} index: {j}")
            prod = right*prev
            rightProduct[j] = prod
            prev = nums[j]
            right = prod
        
        print(leftProduct)
        print(rightProduct)
        for i in range(len(leftProduct)):
            answer.append(leftProduct[i]*rightProduct[i])
        return answer

        
        