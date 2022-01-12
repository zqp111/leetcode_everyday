#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ## 错误, 层序遍历不一定得到正确结果
    #     if root is None: return 0
    #     return self.levelOrder(root.left) + self.levelOrder(root.right) 
    
    # def levelOrder(self, root):
    #     queue = []
    #     if root is None: return 0
    #     queue.append(root)
    #     level = 0
    #     while queue:
    #         l = len(queue)
    #         for i in range(l):
    #             cur = queue.pop(0)
    #             if cur.left: queue.append(cur.left)
    #             if cur.right: queue.append(cur.right)
    #         level += 1
    #     return level
    
        self.result = 0
        self.travel(root)
        return self.result

    def travel(self, node):
        if node is None: return -1

        l = self.travel(node.left) +1
        r = self.travel(node.right) +1
        self.result = max(self.result, r+l)
        return max(r, l)

# @lc code=end

