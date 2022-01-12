#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        self.re = []
        self.binaryTreesearch(root, '')
        return self.re

    def binaryTreesearch(self, root: TreeNode, path):
        if root.left is None and root.right is None:
            if path == '':
                path += str(root.val)
            else:
                path += '->'+str(root.val)
            self.re.append(path)
            return
        if path == '':
            path += str(root.val)
        else:
            path += '->'+str(root.val)
        if root.left is not None:
            self.binaryTreesearch(root.left, path)
        if root.right is not None:  
            self.binaryTreesearch(root.right, path)
# @lc code=end

