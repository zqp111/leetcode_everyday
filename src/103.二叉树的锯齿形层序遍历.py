#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []

        queue = [root]
        level = 0
        result = []
        while queue:
            levelLen = len(queue)
            tmp = []
            for i in range(levelLen):
                if level % 2 == 0:
                    cur = queue.pop(0)
                    tmp.append(cur.val)
                    if cur.left is not None: queue.append(cur.left)
                    if cur.right is not None: queue.append(cur.right)
                else:
                    cur = queue.pop(-1)
                    tmp.append(cur.val)
                    if cur.right is not None: queue.insert(0, cur.right)
                    if cur.left is not None: queue.insert(0, cur.left)
            level += 1
            result.append(tmp.copy())
        return result
                    
# @lc code=end

