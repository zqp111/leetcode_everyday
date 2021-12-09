#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow, fast, p = head, head, head
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if slow == fast:
                break
            
        # print("find cycle")

        while p and slow:
            if slow == p:
                return p
            p = p.next
            slow = slow.next
# @lc code=end

