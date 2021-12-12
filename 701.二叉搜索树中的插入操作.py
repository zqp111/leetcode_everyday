#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        tmp_root = root
        if tmp_root is None:
            return TreeNode(val)
        while tmp_root is not None:
            if tmp_root.val > val:
                if tmp_root.left is not None:
                    tmp_root = tmp_root.left
                else:
                    tmp_root.left = TreeNode(val)
                    return root
                
            else:
                if tmp_root.right is not None:
                    tmp_root = tmp_root.right
                else:
                    tmp_root.right = TreeNode(val)
                    return root
# @lc code=end

