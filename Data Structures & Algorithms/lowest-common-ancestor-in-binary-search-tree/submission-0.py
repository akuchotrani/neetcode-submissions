# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recursion(root):
            if root == None:
                return None
            if root.val == p.val or root.val == q.val:
                # print(f"one of the val found {root.val}")
                return root
            
            if root.val > p.val and root.val > q.val:
                return recursion(root.left)
            elif root.val < p.val and root.val < q.val:
                return recursion(root.right)
            else:
                return root
        
        lca = recursion(root)
        return lca
        