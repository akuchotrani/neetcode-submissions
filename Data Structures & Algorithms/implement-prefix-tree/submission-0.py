class Trie:
    def __init__(self, children = None, isEnd = False):
        self.children = {}
        self.isEnd = isEnd

class PrefixTree:

    def __init__(self):
        self.root = Trie()
        

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Trie()
            current = current.children[char]
        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            # print(f"Searching {char} in {current.children.keys()}")
            if char not in current.children:
                # print(f"-- Not Found {char} in {current.children.keys()}")
                return False
            else:
                current = current.children[char]
        
        if current.isEnd == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            else:
                current = current.children[char]
        return True
        
        