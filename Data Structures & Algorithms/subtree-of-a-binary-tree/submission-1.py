# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def find_root(self, root, subRoot):
        if root == None:
            return None
        # print(f"Traversing {root.val}")
        if root.val == subRoot.val:
            # print(f"Found a common root: {root.val}")
            return root
        res_left = self.find_root(root.left, subRoot)
        if res_left != None:
            return res_left
        res_right = self.find_root(root.right, subRoot)
        if res_right != None:
            return res_right
        
        return None
    
    def compare_sub_tree(self, root, subRoot):
        #print(f"starting compare tree {root.val} and {subRoot.val}")
        if root == None and subRoot == None:
            return True
        
        if root == None:
            print("root is None")
            return False
        elif subRoot == None:
            print("subRoot is None")
            return False
        
        if root.val != subRoot.val:
            print(f"Value mismatch {root.val} and {subRoot.val}")
            return False
        
        res_left = self.compare_sub_tree(root.left, subRoot.left)
        if res_left == False:
            return False
        
        res_right = self.compare_sub_tree(root.right, subRoot.right)
        if res_right == False:
            return False
        
        return True


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subRoot):
            if root == None:
                return False
            
            res = self.compare_sub_tree(root, subRoot)
            if res == True:
                return True
            res_left = self.isSubtree(root.left, subRoot)
            if res_left == True:
                return True
            res_right = self.isSubtree(root.right, subRoot)
            if res_right == True:
                return True

            return False
        
        res = dfs(root, subRoot)
        return res




        