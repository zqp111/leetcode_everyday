# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
            
        last = None
        cur = head
        while cur.next is not None:
            tmp = cur.next
            cur.next = last
            last = cur
            cur = tmp
        cur.next = last
        return cur