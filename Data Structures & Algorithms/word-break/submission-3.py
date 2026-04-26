class Solution:

    def checkIfWordMatches(self, s, word, i):
        counter = 0
        for char in word:
            if i < len(s) and char == s[i]:
                i += 1
                counter += 1
            else:
                return False
        if counter == len(word):
            return True
        
    def recrusive(self, s, wordDict, i):
        print(f"Recursive call for {i}")
        if i == len(s):
            return True
        
        if i in self.memo:
            return self.memo[i]

        for word in wordDict:
            res = self.checkIfWordMatches(s, word, i)
            if res:
                if self.recrusive(s, wordDict, i + len(word)):
                    if i + len(word) not in self.memo:
                        self.memo[i] = True
                    return True
        self.memo[i] = False
        return False
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = {}
        return self.recrusive(s, wordDict, 0)

        