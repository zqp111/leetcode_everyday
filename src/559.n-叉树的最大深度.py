#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
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
    def maxDepth(self, root: 'Node') -> int:
        # print(type(root.children))
        return self.travel(root, 1)

    def travel(self, root, level):
        if root is None: return level -1
        if len(root.children) == 0: return level ## 题目是不是有bug，children == [] 不是None
        return max([self.travel(one_children, level+1) for one_children in root.children])
        
# @lc code=end

