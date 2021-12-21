#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        stack = []
        if root is not None:
            stack.append(root)
        result = []
        while stack:
            length = len(stack)
            tmp = []
            for i in range(length):
                cur = stack.pop(0)
                tmp.append(cur.val)
                if cur.left is not None: stack.append(cur.left)
                if cur.right is not None: stack.append(cur.right)
            result.append(tmp.copy())
        return result
            
# @lc code=end

