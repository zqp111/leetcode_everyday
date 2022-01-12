#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            big = p
            small = q
        else:
            big = q
            small = p
        if root.val >= small.val and root.val <= big.val:
            return root
        if root.val < small.val:
            return self.lowestCommonAncestor(root.right, small, big)
        if root.val > big.val:
            return self.lowestCommonAncestor(root.left, small, big)
# @lc code=end

