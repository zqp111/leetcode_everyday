# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        result = []
        curNode = head
        while curNode is not None:
            result.insert(0, curNode.val)
            curNode = curNode.next
        return result