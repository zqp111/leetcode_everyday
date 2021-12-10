#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.travel(root)


    def travel(self, root:TreeNode):
        queue = [root]
        max_level = -1
        cur_level = 0
        while queue:
            cur_level_length = len(queue) # 当前层节点数
            for _ in range(cur_level_length):
                tmp_node = queue.pop(0)
                if tmp_node.left is not None: queue.append(tmp_node.left)
                if tmp_node.right is not None: queue.append(tmp_node.right)
            cur_level = cur_level + 1
            max_level = max(max_level, cur_level)
        return max_level
# @lc code=end

