# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        def inorder(node):
            if node == None:
                return
            # print(f"In order : {node.val} values: {values}")
            
            if len(values) == k:
                return
            # print(f"Exploring Left : {node.left}")
            inorder(node.left)
            if len(values) < k:
                # print(f"Appending value: {node.val}")
                values.append(node.val)
            # print(f"Exploring Right : {node.right}")
            inorder(node.right)


        
        inorder(root)
        print(f"Final values : {values}")
        return values[k-1]

        