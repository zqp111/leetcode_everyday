#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        new_head = ListNode(next=head)
        mid = new_head
        idx = new_head
        while idx.next:
            print(idx.next.val)
            if idx.next.val < x:
                tmp = idx.next
                idx.next = tmp.next
                tmp.next = mid.next
                mid.next = tmp
                mid = mid.next
            else:
                idx = mid.next

        return new_head.next

# @lc code=end

