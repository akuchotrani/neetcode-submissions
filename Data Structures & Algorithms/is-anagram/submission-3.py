class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_count = [0 for _ in range(26)]

        for i in range(len(s)):
            alpha_count[ord(s[i]) - 97] += 1

        for i in range(len(t)):
            if alpha_count[ord(t[i]) - 97] == 0:
                return False
            else:
                alpha_count[ord(t[i]) - 97] -= 1
        
        for i in range(len(alpha_count)):
            if alpha_count[i] != 0:
                return False

        return True