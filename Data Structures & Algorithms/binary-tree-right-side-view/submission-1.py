# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, root):
        myQueue = deque()
        myQueue.append(root)
        while len(myQueue) > 0:
            children = []
            while len(myQueue) > 0:
                # print(f"myQueue: {myQueue}")
                node = myQueue.popleft()
                child1 = node.left
                child2 = node.right
                if child1 != None:
                    children.append(child1)
                if child2 != None:
                    children.append(child2)
            if len(children) > 0:
                self.answer.append(children[-1].val)
            for node in children:
                myQueue.append(node)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.answer = [root.val]
        self.bfs(root)
        return self.answer
        