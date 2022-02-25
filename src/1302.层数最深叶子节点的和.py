#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        queue = [root]
        while queue:
            ans = 0
            level = len(queue)
            for _ in range(level):
                cur = queue.pop(0)
                ans += cur.val
                if cur.left is not None: queue.append(cur.left)
                if cur.right is not None: queue.append(cur.right)
        return ans
# @lc code=end

