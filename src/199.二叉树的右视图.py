#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None: return []
        queue = [root]
        result = []
        while queue:
            levelLen = len(queue)
            for i in range(levelLen):
                cur = queue.pop(0)
                if i == levelLen - 1: result.append(cur.val)
                if cur.left is not None: queue.append(cur.left)
                if cur.right is not None: queue.append(cur.right)
        return result
# @lc code=end

