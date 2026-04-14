class Solution:
    def getMaxCharacterCount(self, uniqueDict):
        answer = ""
        freq = 0
        for key, val in uniqueDict.items():
            if val > freq:
                answer = key
                freq = val
        return freq
    
    def isValidSlidingWindow(self, left, right, mostFreq, k):
        windowSize = right - left + 1
        if windowSize - mostFreq <= k:
            return True
        else:
            return False

    def characterReplacement(self, s: str, k: int) -> int:
        left  = 0
        right = 0
        answer = 0
        uniqueDict = {}

        while right < len(s):
            if s[right] in uniqueDict:
                uniqueDict[s[right]] += 1
            else:
                uniqueDict[s[right]] = 1
            
            mostFreq = self.getMaxCharacterCount(uniqueDict)
            if self.isValidSlidingWindow(left, right, mostFreq, k):
                answer = max(answer, (right-left)+1)
            else:
                leftChar = s[left]
                uniqueDict[leftChar] -= 1
                if uniqueDict[leftChar] == 0:
                    del uniqueDict[leftChar]
                left += 1
            right += 1
        return answer


            


        