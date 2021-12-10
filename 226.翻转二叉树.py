#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.reverse(root)
        return root

    def reverse(self, root):
        if root is None:
            return

        tmp_node = root.left
        root.left = root.right
        root.right = tmp_node
        if root.left is not None: self.reverse(root.left)
        if root.right is not None: self.reverse(root.right)
# @lc code=end

