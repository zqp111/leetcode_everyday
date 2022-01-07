# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

        return self.travel(head, k)[1]
        
    def travel(self, node, k):
        if node.next is None:
            if k == 1: return True, node
            return False, 1
        f, n = self.travel(node.next, k)
        if f:
            return True, n
        else:
            n = n+1
            if n == k: return True, node
            return False, n