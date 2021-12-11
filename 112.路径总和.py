#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        return self.travel(root, 0, targetSum)
    
    def travel(self, root, sum, targetSum):
        if root is None:
            return False
        sum += root.val
        if root.left is None and root.right is None and sum == targetSum:
            return True
        return self.travel(root.left, sum, targetSum) or self.travel(root.right, sum, targetSum)
# @lc code=end

