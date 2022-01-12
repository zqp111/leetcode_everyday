#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0
        self.travel(root, 0)
        return self.sum
    
    def travel(self, root, tmp):
        if root is None: return
        if root.left is None and root.right is None:
            self.sum += tmp*10+root.val
            return
        tmp = tmp*10 + root.val
        self.travel(root.left, tmp)
        self.travel(root.right, tmp)
# @lc code=end

