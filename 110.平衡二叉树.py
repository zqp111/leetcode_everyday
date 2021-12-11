#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return False if self.travel(root) == -1 else True
    
    def travel(self, root):
        if root is None:
            return 0
        l = self.travel(root.left)
        r = self.travel(root.right)
        if l == -1 or r == -1:
            return -1
        if l - r > 1 or l - r < -1:
            return -1
        return max(l, r)+1

# @lc code=end

