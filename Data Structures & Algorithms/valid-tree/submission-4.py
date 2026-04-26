class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            print("Sufficient Edges are not present")
            return False
        
        if n == 1:
            return True

        
        visited = set()
        
        edge_dict = {}
        for edge in edges:
            if edge[0] not in edge_dict:
                edge_dict[edge[0]] = [edge[1]]
            else:
                edge_dict[edge[0]].append(edge[1])
        
        # For un-directed graph we need to add edges both ways
        for edge in edges:
            if edge[1] not in edge_dict:
                edge_dict[edge[1]] = [edge[0]]
            else:
                edge_dict[edge[1]].append(edge[0])

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in edge_dict[node]:
                dfs(neighbour)
        dfs(edges[0][0])
        if len(visited) != n:
            print(f"Disconnected graph we can only visit {visited}")
            return False
        return True
        
        