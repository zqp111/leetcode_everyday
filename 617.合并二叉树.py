#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        newRoot = TreeNode()
        newRoot = self.__merge(root1, root2, newRoot)

        return newRoot        

    def __merge(self, root1, root2, newRoot):
        if root1 is None and root2 is None:
            newRoot = None
            return
        if root1 is None:
            newRoot = root2
            return newRoot
        if root2 is None:
            newRoot = root1
            return newRoot
        newRoot.val = root1.val + root2.val
        newRoot.left = TreeNode()
        newRoot.right = TreeNode()

        newRoot.left = self.__merge(root1.left, root2.left, newRoot.left)
        newRoot.right = self.__merge(root1.right, root2.right, newRoot.right)
        return newRoot

# @lc code=end

