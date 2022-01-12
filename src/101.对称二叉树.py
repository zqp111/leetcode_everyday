#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.is_same(root.left, root.right)

    def is_same(self, left, right):
        if left is not None and right is not None:
            if left.val == right.val:
                return self.is_same(left.left, right.right) and self.is_same(left.right, right.left)
            else:
                return False
        if left is None and right is None:
            return True
        return False
        
# @lc code=end

