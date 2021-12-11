#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ## 递归
    #     return self.isSearchTree(root, float('-inf'), float('inf'))

    # def isSearchTree(self, root: TreeNode, min_val, max_val): # 每个节点都隐含的包含了上下界
    #     if root is None:
    #         return True
        
    #     if min_val < root.val < max_val:
    #         return self.isSearchTree(root.left, min_val, root.val) and \
    #                 self.isSearchTree(root.right, root.val, max_val)
    #     return False
        ## 非递归
        last = float('-inf')
        stack = []
        cur_node = root
        while stack or cur_node is not None:
            if cur_node is not None: 
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop(-1)
                if cur_node.val <= last:
                    return False 
                last = cur_node.val
                # print('cur_node: ', cur_node.val)
                cur_node = cur_node.right
        return True

# @lc code=end

