class Solution:
    def checkPalindrome(self, left, right, s):
        res = []
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            res.append(s[left:right+1])
            left -= 1
            right += 1
        return len(res)


    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            result += self.checkPalindrome(i, i, s)
            result += self.checkPalindrome(i, i + 1, s)

        return result


        