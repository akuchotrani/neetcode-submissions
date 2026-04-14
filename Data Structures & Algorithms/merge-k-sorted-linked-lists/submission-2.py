# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, firstList, secondList):
        mergedList = []
        counter = 0
        secondPtr = secondList
        while counter != len(firstList) and secondPtr != None:
            if firstList[counter] < secondPtr.val:
                mergedList.append(firstList[counter])
                counter += 1
            else:
                mergedList.append(secondPtr.val)
                secondPtr = secondPtr.next
        
        while counter != len(firstList):
            mergedList.append(firstList[counter])
            counter += 1

        while secondPtr != None:
            mergedList.append(secondPtr.val)
            secondPtr = secondPtr.next
        return mergedList
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        mergedList = []
        for i in range(len(lists)):
            mergedList = self.mergeTwoLists(mergedList, lists[i])
            # print(f"Each iteration : {mergedList}")
        
        answer = None
        prevNode = None
        for i in range(len(mergedList)):
            node = ListNode(mergedList[i])
            if prevNode != None:
                prevNode.next = node
            if prevNode == None:
                answer = node
            prevNode = node
            
        print(f"Final answer: {mergedList}")

        return answer
            
