#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        nowLast = 0
        while stack or cur is not None:
            if cur is not None: 
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop(-1)
                nowLast += 1
                if nowLast == k: return cur.val
                cur = cur.right
        

# @lc code=end

