# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calculateMaxSum(self, node):
        if node == None:
            return 0
        # print(f"node.val: {node.val}")
        left_sum = max(self.calculateMaxSum(node.left), 0)
        right_sum = max(self.calculateMaxSum(node.right), 0)
        combined_sum = left_sum + right_sum + node.val
        temp = max(combined_sum, combined_sum)
        self.answer = max(self.answer, temp)
        # print(f"Node: {node.val} left_sum: {left_sum} right_sum: {right_sum} max: {temp} answer: {self.answer}")
        return node.val + max(left_sum, right_sum)



    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = float("-inf")
        self.calculateMaxSum(root)

        return self.answer
        