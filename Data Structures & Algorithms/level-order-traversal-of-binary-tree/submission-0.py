# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        myQueue = deque()
        myQueue.append([root])
        result = []

        while len(myQueue) > 0:
            nodes = myQueue.pop()
            children = []
            values = []
            for node in nodes:
                if node != None:
                    values.append(node.val)
                if node.left != None:
                    children.append(node.left)
                if node.right != None:
                    children.append(node.right)
            if len(children) > 0:
                myQueue.append(children)
            result.append(values)
        return result