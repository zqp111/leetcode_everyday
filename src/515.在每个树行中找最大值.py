#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        queue = [root]

        ans = []

        while queue:
            level = len(queue)
            tmp = queue[0].val
            for i in range(level):
                cur = queue.pop(0)
                tmp = max(tmp, cur.val)
                if cur.left is not None: queue.append(cur.left)
                if cur.right is not None: queue.append(cur.right)
            ans.append(tmp)
        return ans


# @lc code=end

