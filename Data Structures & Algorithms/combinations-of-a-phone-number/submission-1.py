class Solution:

    def dfs(self, digitsList, combo, expectedLength):
        # print(f"DFS called : {digitsList} combo:{combo}")
        if len(digitsList) == 0 and len(combo) == expectedLength:
            self.answer.append(combo[::-1].lower())
            return
        
        currDigit = digitsList.pop()
        for char in self.digitDict[currDigit]:
            combo+=char
            self.dfs(digitsList.copy(), combo, expectedLength)
            combo=combo[:-1]


    def letterCombinations(self, digits: str) -> List[str]:
        self.answer = []
        self.digitDict = {}
        self.digitDict['2'] = ['A', 'B', 'C']
        self.digitDict['3'] = ['D', 'E', 'F']
        self.digitDict['4'] = ['G', 'H', 'I']
        self.digitDict['5'] = ['J', 'K', 'L']
        self.digitDict['6'] = ['M', 'N', 'O']
        self.digitDict['7'] = ['P', 'Q', 'R', 'S']
        self.digitDict['8'] = ['T', 'U', 'V']
        self.digitDict['9'] = ['W', 'X', 'Y', 'Z']
        digitsList = []
        for i in range(len(digits)):
            digitsList.append(digits[i])
        if len(digits) == 0:
            return self.answer
        self.dfs(digitsList, "", len(digitsList))
        return self.answer
        