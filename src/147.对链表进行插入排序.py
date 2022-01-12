#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
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

