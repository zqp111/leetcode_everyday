#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        depth = self.bfs(root)

        return depth

    def bfs(self, root):
        if root is None:
            return 0
        # min_depth = float("inf")
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)

            if not node.left and not node.right:
                return level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
# @lc code=end

