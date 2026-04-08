# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head == None or head.next == None:
            return
        
        turtle_ptr = head
        rabbit_ptr = head.next

        while rabbit_ptr != None and rabbit_ptr.next != None:
            turtle_ptr = turtle_ptr.next
            rabbit_ptr = rabbit_ptr.next.next

        print(f"Found the midpoint at {turtle_ptr.val}")

        mid_ptr = turtle_ptr.next
        turtle_ptr.next = None
        prev_ptr = None
        next_ptr = None
        last_node_ptr = None
        while mid_ptr != None:
            if mid_ptr != None:
                last_node_ptr = mid_ptr
            print(f"last_node_ptr: {last_node_ptr.val}")
            next_ptr = mid_ptr.next
            mid_ptr.next = prev_ptr
            prev_ptr = mid_ptr
            mid_ptr = next_ptr
        
        temp_1 = None
        temp_2 = None
        while head != turtle_ptr:
            print(f"head: {head.val} last_node_ptr: {last_node_ptr.val}")
            temp_1 = head.next
            head.next = last_node_ptr
            temp_2 = last_node_ptr.next
            last_node_ptr.next = temp_1
            last_node_ptr = temp_2
            head = temp_1
        
        if last_node_ptr != None:
            head.next = last_node_ptr
        

            



        