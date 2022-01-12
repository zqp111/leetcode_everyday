#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        ##递归
    #     self.min_sub = float('inf')
    #     self.travel(root, [float('-inf')]) # 这里用列表，列表等数据结构传参为指针
                                             # int等数据类型传参为数值引用
    #     return self.min_sub

    # def travel(self, root, last_val):
    #     if root is None:
    #         return 
    #     self.travel(root.left, last_val)
    #     print('last: ', last_val)
    #     self.min_sub = min(self.min_sub, root.val-last_val[0])
    #     last_val[0] = root.val
    #     self.travel(root.right, last_val)

        ## 非递归
        last = float('-inf')
        min_sub = float('inf')
        stack = []
        cur_node = root
        while stack or cur_node is not None:
            if cur_node is not None: 
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop(-1)
                min_sub = min(cur_node.val - last, min_sub)
                last = cur_node.val
                # print('cur_node: ', cur_node.val)
                cur_node = cur_node.right
        return min_sub

# @lc code=end

