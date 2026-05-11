# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, maxValue):
        if root == None:
            return
        
        if root.val >= maxValue:
            maxValue = root.val
            self.answer += 1
        
        self.dfs(root.left, maxValue)
        self.dfs(root.right, maxValue)



    def goodNodes(self, root: TreeNode) -> int:
        self.answer = 0
        maxVal = root.val

        self.dfs(root, maxVal)
        return self.answer
        