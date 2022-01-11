#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return head
        cur = head
        lenCount = 0
        prevNode = None
        while cur:
            lenCount += 1
            prevNode = cur
            cur = cur.next
        prevNode.next = head
        k %= lenCount
        cur = head
        for i in range(lenCount-k):
            prevNode = cur
            cur = cur.next
        prevNode.next = None
        return cur
# @lc code=end

