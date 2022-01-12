#
# @lc app=leetcode.cn id=1382 lang=python3
#
# [1382] 将二叉搜索树变平衡
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.list = []
        self.travel(root)
        return self.buildTree(self.list)
        
    def travel(self, root):
        if root is None:
            return 
        self.travel(root.left)
        self.list.append(root.val)
        self.travel(root.right)
    
    def buildTree(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        Node = TreeNode(nums[mid])
        Node.left = self.buildTree(nums[:mid])
        Node.right = self.buildTree(nums[mid+1:])
        return Node
# @lc code=end

