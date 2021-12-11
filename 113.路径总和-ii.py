#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.re = []
        self.travel(root, 0, targetSum, [])
        return self.re
    
    def travel(self, root, pathSum, targetSum, tmpPath):
        # print(tmpPath, pathSum)
        if root is None:
            return

        tmpPath.append(root.val)
        pathSum += root.val

        if root.left is None and root.right is None and pathSum == targetSum:
            self.re.append(tmpPath.copy())
            pathSum -= root.val
            tmpPath.pop(-1)
            return
        
        self.travel(root.left, pathSum, targetSum, tmpPath)
        self.travel(root.right, pathSum, targetSum, tmpPath)
        pathSum -= root.val
        tmpPath.pop(-1)
# @lc code=end

