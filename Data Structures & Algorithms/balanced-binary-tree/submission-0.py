# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, node):
        if node == None:
            return 0
        # print(f"DFS called for {node.val}")
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        # print(f"Height diff for node:{node.val} is {right-left}")
        if abs(right - left) > 1:
            self.isBalanced = False
        return 1 + max(right, left)



    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        self.dfs(root)
        return self.isBalanced