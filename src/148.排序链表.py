#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## 超时
        newHead = ListNode(val=float('-inf'))

        cur = head
        while cur:
            # print(cur.val)
            tmp = cur
            cur = cur.next
            self.insert(newHead, tmp)
            
        return newHead.next

    def insert(self, newHead, tmp):
        cur = newHead
        while cur:
            if cur.val < tmp.val and (cur.next is None or cur.next.val >= tmp.val):
                tmp.next = cur.next
                cur.next = tmp
                break
            cur = cur.next
# @lc code=end

