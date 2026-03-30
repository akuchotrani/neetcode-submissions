# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        second = list2

        result = ListNode()
        head = result

        while first != None and second != None:
            if first.val <= second.val:
                result.next = first
                result = result.next
                first = first.next
            elif second.val < first.val:
                result.next = second
                result = result.next
                second = second.next
            else:
                result.next = first
                result = result.next
                result.next = second
                result = result.next
                first = first.next
                second = second.next

        if first != None:
            result.next = first

        if second != None:
            result.next = second
        
        
        return head.next


        