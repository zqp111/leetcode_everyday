#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l, head = self.get_next(head, n)
        return head

    def get_next(self, node, n):
        if node is None:
            return 0, None
        i, next = self.get_next(node.next, n)
        i += 1
        if i == n:
            return i, next
        node.next = next
        return i, node

# @lc code=end

