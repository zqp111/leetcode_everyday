#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        newHead = ListNode(0, head)
        cur = head
        prevNode = newHead
        count = 0
        while cur:
            count += 1
            # print(cur, count)
            if count == k:
                count = 0
                prevNode = self.reverse(prevNode, cur.next)
                cur = prevNode.next
            else:
                cur = cur.next
        return newHead.next

    def reverse(self, prevNode, nextNode):
        cur = prevNode.next
        while cur.next is not nextNode:
            tmp = cur.next.next
            cur.next.next = prevNode.next
            prevNode.next = cur.next
            cur.next = tmp
        # print(cur.val)
        return cur
        


# @lc code=end

