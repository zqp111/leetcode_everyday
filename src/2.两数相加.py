#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        begin = ListNode()
        re = ListNode()
        re.next = begin
        c = 0
        while l1 != None or l2 != None:
            re = re.next
            if l1 == None:
                tmp = l2.val +c
                l2 = l2.next
            elif l2 == None:
                tmp = l1.val +c
                l1 = l1.next
            else:
                tmp = l1.val + l2.val + c
                l1 = l1.next
                l2 = l2.next
            if tmp < 10:
                re.val = tmp
                c = 0 
            else:
                re.val = tmp -10
                c = 1
            re.next = ListNode()
        if c == 0:
            re.next = None
        else:
            re.next.val =1
        return begin


# @lc code=end

