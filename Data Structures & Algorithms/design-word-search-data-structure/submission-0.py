class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                node = TrieNode()
                curr.children[char] = node
                curr = curr.children[char]
        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(i, word, node):
            if i == len(word):
                return node.isEndOfWord
            char = word[i]
            if char == ".":
                for child in node.children.values():
                    if dfs(i+1, word, child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                else:
                    return dfs(i+1, word, node.children[char])
        curr = self.root
        return dfs(0, word, curr)
        
        
