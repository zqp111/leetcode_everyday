#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        newHead = ListNode()
        cur = newHead
        
        ## 去除空链表
        index = 0
        while index < len(lists):
            if lists[index] is None:
                lists.pop(index)
            else:
                index += 1
        
        while lists:
            tmpMinNode = lists[0]
            minIndex = 0
            for i, node in enumerate(lists):
                if node.val < tmpMinNode.val:
                    tmpMinNode = node
                    minIndex = i
            cur.next = tmpMinNode
            if tmpMinNode.next is None:
                lists.pop(minIndex)
            else:
                lists[minIndex] = tmpMinNode.next
            cur = cur.next

        return newHead.next
# @lc code=end

