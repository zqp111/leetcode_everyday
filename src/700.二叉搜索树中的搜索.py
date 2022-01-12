#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        searchedNode = root
        while searchedNode is not None:
            if val < searchedNode.val:
                searchedNode = searchedNode.left
            elif val > searchedNode.val:
                searchedNode = searchedNode.right
            else:
                return searchedNode
        return None
# @lc code=end

