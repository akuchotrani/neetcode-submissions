# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def DFS(x, y):
            if x == None and y == None:
                return True
            
            if x == None:
                return False
            
            if y == None:
                return False
            
            if x.val != y.val:
                print(f" value mismatch {x.val} and {y.val}")
                return False
            
            res_left = DFS(x.left, y.left)
            if res_left == False:
                return False

            res_right = DFS(x.right, y.right)
            if res_right == False:
                return False
            
            return True
        
        res = DFS(p,q)
        return res
        
    
        