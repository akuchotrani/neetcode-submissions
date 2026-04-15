# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        myHeap = []
        def dfs(node):
            if node == None:
                return
            
            if len(myHeap) < k:
                print(f"Pushing new element: {node.val}")
                heapq.heappush(myHeap, -1 * node.val)
            else:
                top = myHeap[0]
                if node.val < -1 * top:
                    popped = heapq.heappop(myHeap)
                    print(f"Len of heap reached so popping: {-1 * popped}")
                    print(f"Pushing : {node.val}")
                    heapq.heappush(myHeap, -1 * node.val)
                else:
                    print(f"Do nothing for node: {node.val}")
            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return -1 * heapq.heappop(myHeap)
                
        