#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        maxVal, maxValArg = self.__argmax(nums)
        root = TreeNode(maxVal)
        root.left = self.constructMaximumBinaryTree(nums[:maxValArg])
        root.right = self.constructMaximumBinaryTree(nums[maxValArg+1:])
        return root

    def __argmax(self, nums: List[int]) -> TreeNode:
        maxNum = float('-inf')
        maxNumArg = -1
        for i, num in enumerate(nums):
            if num > maxNum:
                maxNumArg = i
                maxNum = num
        return maxNum, maxNumArg

# @lc code=end

