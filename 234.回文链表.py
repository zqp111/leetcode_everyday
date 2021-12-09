#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        # 寻找中间节点
        fast, mid = head, head
        while fast:
            fast = fast.next
            mid = mid.next
            if not fast:
                break
            fast = fast.next
            
        # print(mid.val)
        # 反转后半段链表
        pre = None
        current = mid
        while current:
            tmp = current.next
            current.next = pre
            pre = current
            current = tmp
            

        begin = head
        mid = pre
        
        while mid:
            if mid.val != begin.val:
                return False
            mid = mid.next
            begin = begin.next
        return True
        
        

# @lc code=end

