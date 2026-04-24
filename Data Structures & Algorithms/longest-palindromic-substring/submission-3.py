class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLength = 0
        if len(s) == 1:
            return s[0]
        for i in range(len(s)):
            # odd scenario
            left = i
            right = i
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if right - left + 1 > resLength:
                    res = s[left:right+1]
                    resLength = right - left + 1
                left -= 1
                right += 1
            
            # Even Scenario
            left = i
            right = i + 1
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if right - left + 1 > resLength:
                    res = s[left:right+1]
                    resLength = right - left + 1
                left -= 1
                right += 1
        return res
        