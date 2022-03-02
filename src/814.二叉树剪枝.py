#
# @lc app=leetcode.cn id=814 lang=python3
#
# [814] 二叉树剪枝
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.travel(root)

    def travel(self, node):
        if node is None: return None

        node.left = self.travel(node.left)
        node.right = self.travel(node.right)


        if node.left is None and node.right is None:
            if node.val == 0:
                return None
        return node
# @lc code=end

