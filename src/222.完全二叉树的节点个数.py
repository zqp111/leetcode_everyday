#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:

    ## 遍历方式
    #     return self.travel(root)

    # def travel(self, root:TreeNode):
    #     node_num = 0
    #     queue = []
    #     if root is not None:
    #         queue.append(root)
    #     while queue:
    #         tmp_node = queue.pop(0)
    #         node_num += 1
    #         if tmp_node.left is not None: queue.append(tmp_node.left)
    #         if tmp_node.right is not None: queue.append(tmp_node.right)
    #     return node_num

    ## 非遍历, 利用完全二叉树的性质
        
        return self.get_node_num(root)
    
    def __is_complete(self, root):
        if root is None:
            return True, 0
        left, right = root.left, root.right
        l_depth, r_depth = 1, 1
        while left is not None:
            left = left.left
            l_depth += 1
        while right is not None:
            right = right.right
            r_depth += 1
        return l_depth == r_depth, (2 << (l_depth-1)) -1

    def get_node_num(self, root: TreeNode) -> int:
        f, num = self.__is_complete(root)
        if f:
            return num
        return 1 + self.get_node_num(root.left) + self.get_node_num(root.right)

# @lc code=end

