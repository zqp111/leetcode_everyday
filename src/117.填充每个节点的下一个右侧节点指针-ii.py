#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return None
        startNode = root
        while startNode is not None:
            self.nextStartNode, self.lastNode = None, None
            cur = startNode
            while cur is not None:
                if cur.left is not None:
                    self.doConnect(cur.left)
                    # print('out do: ', self.lastNode.val)
                if cur.right is not None:
                    self.doConnect(cur.right)
                    # print('out do: ', self.lastNode.val)
                cur = cur.next
            startNode = self.nextStartNode
        return root
                    
    
    def doConnect(self, cur):
        if self.lastNode is not None:
            self.lastNode.next = cur
        if self.nextStartNode is None: 
            self.nextStartNode = cur
        self.lastNode = cur
        # print('in do :', last.val)
# @lc code=end

