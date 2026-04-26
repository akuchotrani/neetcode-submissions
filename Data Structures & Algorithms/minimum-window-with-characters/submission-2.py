class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needDict = {}
        haveDict = {}
        for char in t:
            if char in needDict:
                needDict[char] += 1
            else:
                needDict[char] = 1
        for char in t:
            if char not in haveDict:
                haveDict[char] = 0
        need = len(needDict)
        have = 0
        left = 0
        right = 0
        result = ""
        window = float('inf')

        while right < len(s):
            if s[right] in needDict:
                haveDict[s[right]] += 1
                if haveDict[s[right]] == needDict[s[right]]:
                    have += 1
                while left <= right and have == need:
                    if right-left < window:
                        result = s[left:right + 1]
                        window = right - left + 1
                    if s[left] in haveDict:
                        haveDict[s[left]] -= 1
                        if haveDict[s[left]] < needDict[s[left]]:
                            have -= 1
                    left += 1
            right += 1
        return result



        