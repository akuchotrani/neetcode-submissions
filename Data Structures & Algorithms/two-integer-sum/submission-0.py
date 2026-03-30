class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        answer = []
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in myDict:
                answer.append(myDict[remainder])
                answer.append(i)
                return answer
            else:
                myDict[nums[i]] = i
        
        return []
        