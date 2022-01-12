#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = float('-inf')

        def travel(node):
            if node is None: return 0
            left = travel(node.left)
            right = travel(node.right)
            self.result = max(self.result, max(0, left)+max(right, 0)+node.val)
            return node.val+max(0, left, right)
        
        travel(root)
        return self.result
# @lc code=end

