# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode()
        curNode=head
        while list1 and list2:
            if list1.val < list2.val:
                curNode.next = list1
                list1 = list1.next
            else:
                curNode.next = list2
                list2 = list2.next
            curNode = curNode.next
        if list1 is None: curNode.next = list2
        else: curNode.next = list1
        return head.next
