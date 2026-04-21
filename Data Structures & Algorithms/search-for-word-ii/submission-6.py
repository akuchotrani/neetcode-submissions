class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:

    def __init__(self):
        self.root = TrieNode()

    def addEachWordToTrie(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def searchPossibleWords(self, row, col, board, traversedWord, trieNode):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            # print(f"Out of bounds r:{row} c:{col}")
            return

        # print(f"Checking row:{row} col:{col}")
        
        if board[row][col] in trieNode.children:
            char = board[row][col]
            traversedWord += char
            # print(f"Found the char: {char} traversedword: {traversedWord} trying to find neighbours")
            nextNode = trieNode.children[char]
            if nextNode.endOfWord:
                self.result.add(traversedWord)
                nextNode.endOfWord = False
                # print(f"!!!Answer found: {traversedWord}")
            # Marking the cell as # so that it does not visit the same cell again.
            board[row][col] = "#"
            self.searchPossibleWords(row-1, col, board, traversedWord, trieNode.children[char])
            self.searchPossibleWords(row+1, col, board, traversedWord, trieNode.children[char])
            self.searchPossibleWords(row, col-1, board, traversedWord, trieNode.children[char])
            self.searchPossibleWords(row, col+1, board, traversedWord, trieNode.children[char])
            # Unmakking the cell
            board[row][col] = char



        

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result = set()
        for word in words:
            self.addEachWordToTrie(word)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                # print(f"-- Starting Search for row: {row} col: {col}")
                self.searchPossibleWords(row, col, board, "", self.root)
        
        return list(self.result)
        