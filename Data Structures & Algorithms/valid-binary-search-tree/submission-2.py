# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minVal, maxVal):
            if node == None:
                return True
            
            if not (minVal < node.val < maxVal):
                print(f"Node: {node.val} does not satisfy the range {minVal}-{maxVal} ")
                return False
            
            result_left = dfs(node.left, minVal, node.val)
            if result_left == False:
                return False
            
            result_right = dfs(node.right, node.val, maxVal)
            if result_right == False:
                return False
            
            return True
        return dfs(root, float("-inf"), float("inf"))
        