#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        newHead = ListNode()
        last = newHead
        curFirst = head
        if curFirst is None:
            return head
        curSecond = head.next
        if curSecond is None:
            return head
        while curSecond is not None:
            curFirst.next = curSecond.next
            curSecond.next = curFirst
            last.next = curSecond
            last = curFirst
            curFirst = curFirst.next
            if curFirst is not None:
                curSecond = curFirst.next
            else:
                break
        return newHead.next
        
# @lc code=end

