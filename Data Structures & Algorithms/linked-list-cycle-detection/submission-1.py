# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False

        turtle_ptr = head
        rabbit_ptr = head.next

        while turtle_ptr != None and rabbit_ptr != None:
            if turtle_ptr == rabbit_ptr:
                print(f"Cycle found at : {turtle_ptr.val}")
                return True
            turtle_ptr = turtle_ptr.next
            if rabbit_ptr.next != None:
                rabbit_ptr = rabbit_ptr.next.next
            else:
                print("Rabbit reached the end")
                return False
        
        return False
        