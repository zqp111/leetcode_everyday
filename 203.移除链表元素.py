#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        last = ListNode(1)
        new_head = last
        cur = head
        last.next = cur
        while cur is not None:
            if cur.val == val:
                last.next = cur.next
                cur = cur.next
            else:
                last = cur
                cur = cur.next
        return new_head.next
# @lc code=end

