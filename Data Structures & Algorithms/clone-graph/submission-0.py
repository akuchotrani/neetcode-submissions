"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def traverseGraph(self, node):
        if node.val not in self.isVisited:
            self.isVisited.add(node.val)
        else:
            return
        
        new_node = Node(node.val)
        self.copiedNodes[new_node.val] = new_node
        for neighbor in node.neighbors:
            self.traverseGraph(neighbor)
            new_node.neighbors.append(self.copiedNodes[neighbor.val])

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        self.isVisited = set()
        self.copiedNodes = {}
        self.traverseGraph(node)
        return self.copiedNodes[1]
        
        