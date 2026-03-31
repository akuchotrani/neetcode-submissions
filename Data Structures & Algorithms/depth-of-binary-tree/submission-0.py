# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        result = 0
        stack = [(root, 1)]

        while stack:
            node = stack.pop()
            result = max(result, node[1])

            if node[0] and node[0].left != None:
                stack.append((node[0].left, node[1]+1))
            
            if node[0] and node[0].right != None:
                stack.append((node[0].right, node[1]+1))
        return result

        