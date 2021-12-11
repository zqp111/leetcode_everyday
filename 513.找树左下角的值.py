#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return self.travel(root)

    def travel(self, root):
        queue = []
        if root is not None:
            queue.append(root)
        left_value = None
        while queue:
            length = len(queue)
            
            for i in range(length):
                tmp_node = queue.pop(0)
                if i == 0:
                    left_value = tmp_node.val
                if tmp_node.left is not None: queue.append(tmp_node.left)
                if tmp_node.right is not None: queue.append(tmp_node.right)
        return left_value
# @lc code=end

