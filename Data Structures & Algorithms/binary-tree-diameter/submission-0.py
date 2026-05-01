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
        
        res_left = self.dfs(node.left)
        res_right = self.dfs(node.right)
        res_combined = res_left + res_right
        self.diameter = max(self.diameter, res_combined)
        return 1 + max(res_left, res_right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        result = self.dfs(root)
        return self.diameter
        