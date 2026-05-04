class Solution:
    def checkPalindrome(self, left, right, s):
        count = 0
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            count += 1
            left -= 1
            right += 1
        return count


    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            result += self.checkPalindrome(i, i, s)
            result += self.checkPalindrome(i, i + 1, s)

        return result


        