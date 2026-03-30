class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        answer = 0

        for num in my_set:
            if num - 1 in my_set:
                continue
            else:
                counter = 0
                iter = num
                while iter in my_set:
                    counter += 1
                    iter += 1
                answer = max(counter, answer)
        
        return answer
        