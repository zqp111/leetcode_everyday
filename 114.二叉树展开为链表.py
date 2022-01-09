#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        if root is not None: stack.append(root)
        newRoot = TreeNode()
        last = newRoot
        while stack:
            cur = stack.pop(-1)
            last.left, last.right = None, cur
            if cur.right is not None: stack.append(cur.right)
            if cur.left is not None: stack.append(cur.left)
            last = cur
        return newRoot.right

# @lc code=end

