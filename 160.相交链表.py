#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA = headA
        nodeB = headB
        switch = False
        while nodeA != nodeB:
            if nodeA.next is None:
                if switch:
                    return None
                nodeA = headB
                switch = True
            else:
                nodeA = nodeA.next
            if nodeB.next is None:
                nodeB = headA
            else:
                nodeB = nodeB.next
        return nodeA
# @lc code=end

