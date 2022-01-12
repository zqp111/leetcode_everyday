#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.result = 0
        self.travel(root, [0], targetSum)
        return self.result

    def travel(self, node, paths, targetSum):
        if node is None: return
        nodeSum = node.val + paths[-1] 
        for preSum in paths:
            if nodeSum - preSum == targetSum:
                self.result += 1
        paths.append(nodeSum)
        self.travel(node.left, paths, targetSum)
        self.travel(node.right, paths, targetSum)
        paths.pop(-1)
# @lc code=end

