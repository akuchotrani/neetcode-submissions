# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        endPtr = head

        for i in range(n):
            endPtr = endPtr.next
        
        prevPtr = None
        currPtr = head

        while endPtr != None:
            prevPtr = currPtr
            currPtr = currPtr.next
            endPtr = endPtr.next
        
        if prevPtr == None and currPtr.next==None:
            return None
        elif prevPtr == None and currPtr.next != None:
            print(f"Before {head.val} and {currPtr.val}")
            head = currPtr.next
            print(f"After {head.val} and {currPtr.val}")

        else:
            prevPtr.next = currPtr.next
        
        return head

        