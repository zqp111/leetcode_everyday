# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        newHead = ListNode()
        newHead.next = head
        last =newHead
        cur = head
        while cur:
            if cur.val == val:
                last.next = cur.next
            last = cur
            cur = cur.next
        return newHead.next
