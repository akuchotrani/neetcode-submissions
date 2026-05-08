# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ptr = l1
        l2_ptr = l2
        carry = 0
        start = ListNode()
        curr = start
        while l1_ptr and l2_ptr:
            val_1 = l1_ptr.val
            val_2 = l2_ptr.val
            val = val_1 + val_2 + carry
            if val > 9:
                val = val%10
                carry = 1
            else:
                carry = 0
            
            node = ListNode(val)
            curr.next = node
            curr = node
            l1_ptr = l1_ptr.next
            l2_ptr = l2_ptr.next
        
        remaining_ptr = l1_ptr if l1_ptr != None else l2_ptr if l2_ptr != None else None
        while remaining_ptr:
            val = remaining_ptr.val + carry
            if val > 9:
                val = val%10
                carry = 1
            else:
                carry = 0
            node = ListNode(val)
            curr.next = node
            curr = node
            remaining_ptr = remaining_ptr.next
        
        if carry != 0:
            node = ListNode(carry)
            curr.next = node
        
        return start.next



            

        