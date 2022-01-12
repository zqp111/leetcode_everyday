#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
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
        if root is None:
            return None

        stack = [root]
        while stack:
            n = len(stack)
            for i in range(n):
                if i == 0:
                    cur = stack.pop(0)
                    last = cur
                else:
                    cur = stack.pop(0)
                    last.next = cur
                    last = cur
                if cur.left is not None: stack.append(cur.left)
                if cur.right is not None: stack.append(cur.right)

        return root
        
        
# @lc code=end

