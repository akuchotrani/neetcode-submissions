class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {}
        for word in words:
            for char in word:
                if char not in adjList:
                    adjList[char] = set()
        
        for key, val in adjList.items():
            print(f"adjList {key}:{val}")
        

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minLength = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ""
            for j in range(minLength):
                if word1[j] != word2[j]:
                    adjList[word1[j]].add(word2[j])
                    break
        
        print("#### ADJ list after building ####")
        for key, val in adjList.items():
            print(f"adjList {key}:{val}")
        


        print("--- Peform DFS search -----")
        finalResult = list()
        visit = {}
        def dfs(character):
            if character in visit:
                return visit[character]
            # Now marking visit to true for current dfs path
            visit[character] = True
            for neighbour in adjList[character]:
                result = dfs(neighbour)
                if result:
                    return True
            visit[character] = False
            finalResult.append(character)
            print(f"No cycle detected so returning False")
            return False

        for key,val in adjList.items():
            if dfs(key):
                return ""

        finalResult.reverse()
        print(f"final: {finalResult}")
        return "".join(finalResult)
        