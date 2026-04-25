# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.result = ""
        def preorder(node):
            if node == None:
                self.result += "N" + ","
                return
            self.result += str(node.val) + ","
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        self.result = self.result.rstrip(',')
        print(f"result: {self.result}")
        return self.result

    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        elements = data.split(',')
        root = None
        self.counter = 0
        def dfs():
            if elements[self.counter] == 'N':
                self.counter += 1
                return
            node = TreeNode(int(elements[self.counter]))
            self.counter += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
