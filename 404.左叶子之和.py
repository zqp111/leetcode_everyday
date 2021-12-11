#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        self.travel(root)
        return self.sum

    def travel(self, root):
        # print(root.val)
        if root is None: return 0

        if root.left is None and root.right is None:
            # print('leave: {}'.format(root.val))
            return root.val

        self.sum = self.travel(root.left) + self.sum
        # print('root: {} sum: {}'.format(root.val, self.sum))
        self.travel(root.right)

        return 0
        
# @lc code=end

