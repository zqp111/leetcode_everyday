#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 递归
    #     self.sum = 0
    #     self.travel(root)
    #     return root

    # def travel(self, root):
    #     if root is None:
    #         return
    #     self.travel(root.right)
    #     self.sum += root.val
    #     root.val = self.sum
    #     self.travel(root.left)

        ## 非递归
        sum = 0
        cur_node = root
        stack = []
        while stack or cur_node is not None:
            if cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.right
            else:
                cur_node = stack.pop(-1)
                # print(cur_node.val)
                sum += cur_node.val
                cur_node.val = sum
                cur_node = cur_node.left
        return root
# @lc code=end

