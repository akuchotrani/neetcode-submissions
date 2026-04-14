class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueDict = {}
        answer = 0
        left = 0
        right = 0

        while right < len(s):
            print(f"left: {left} right: {right} s[right]: {s[right]} uniqueDict: {uniqueDict}")
            if s[right] not in uniqueDict:
                uniqueDict[s[right]] = right
            else:
                print(f"Duplicate found : {s[right]}")
                end_idx = uniqueDict[s[right]]
                for i in range(left, end_idx+1):
                    del uniqueDict[s[i]]
                left = end_idx + 1
                uniqueDict[s[end_idx]] = right
            answer = max(answer, (right-left) + 1)
            right += 1
        return answer

                


        