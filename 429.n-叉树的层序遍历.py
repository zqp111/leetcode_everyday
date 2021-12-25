#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        stack = []
        result = []
        if root is not None:
            stack.append(root)

        while stack:
            length = len(stack)
            tmp = []
            for _ in range(length):
                cur = stack.pop(0)
                tmp.append(cur.val)
                for i in range(len(cur.children)):
                    stack.append(cur.children[i])
            result.append(tmp)
        return result
        
# @lc code=end

