class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        myDict = {}
        for edge in edges:
            if edge[0] not in myDict:
                myDict[edge[0]] = [edge[1]]
            else:
                myDict[edge[0]].append(edge[1])
        
        for edge in edges:
            if edge[1] not in myDict:
                myDict[edge[1]] = [edge[0]]
            else:
                myDict[edge[1]].append(edge[0])
        
        print(myDict)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            # Isolated node with no edges
            if node not in myDict:
                return
            for neighbour in myDict[node]:
                dfs(neighbour)
        
        counter = 0
        for node in range(n):
            if node in visited:
                continue
            dfs(node)
            counter += 1

        return counter

        