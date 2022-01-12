#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if self.isSameTree(cur, subRoot):
                return True
            if cur.left is not None: queue.append(cur.left)
            if cur.right is not None: queue.append(cur.right)
        return False

    def isSameTree(self, rootA, rootB):
        if rootA is None and rootB is None:
            return True
        if rootA is None or rootB is None:
            return False
        if rootA.val != rootB.val:
            return False
        return self.isSameTree(rootA.left, rootB.left) \
                and self.isSameTree(rootA.right, rootB.right)
# @lc code=end

