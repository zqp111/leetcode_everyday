#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            ## 非递归
        # if root is None:
        #     return None

        # searchedNode = root
        # fatherNode = None
        # from_root = 0
        # while searchedNode.val != key:
        #     if searchedNode.val < key:
        #         fatherNode = searchedNode
        #         from_root = 2
        #         searchedNode = searchedNode.right
        #     elif searchedNode.val > key:
        #         fatherNode = searchedNode
        #         from_root = 1
        #         searchedNode = searchedNode.left
        #     if searchedNode is None:
        #         return root

        # left = searchedNode.left
        # right = searchedNode.right

        # if right is None:
        #     if from_root == 0:
        #         return left
        #     elif from_root == 1:
        #         fatherNode.left = left
        #     else:
        #         fatherNode.right = left
        #     return root
        # else:
        #     minRightNode = right
        #     rightFather = searchedNode
        #     if minRightNode.left is None:
        #         searchedVal = minRightNode.val
        #         # print('shanchu')
        #         right = minRightNode.right
        #     else:
        #         while True:
        #             if minRightNode.left is not None:
        #                 rightFather = minRightNode
        #                 minRightNode = minRightNode.left
        #             else:
        #                 searchedVal = minRightNode.val
        #                 rightFather.left = minRightNode.right
        #                 break
        #     if from_root == 0:
        #         newNode = TreeNode(searchedVal)
        #         newNode.left = left
        #         newNode.right = right
        #         minRightNode = None
        #         return newNode
        #     elif from_root == 1:
        #         newNode = TreeNode(searchedVal)
        #         newNode.left = left
        #         newNode.right = right
        #         fatherNode.left = newNode
        #         minRightNode = None
        #     else:
        #         newNode = TreeNode(searchedVal)
        #         newNode.left = left
        #         newNode.right = right
        #         fatherNode.right = newNode
        #         minRightNode = None
        #     return root
            ## 递归
        if root is None:
            return None
        
        if root.val == key:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                cur_node = root.right
                while cur_node.left is not None:
                    cur_node = cur_node.left
                cur_node.left = root.left
                return root.right
        if root.val < key: root.right = self.deleteNode(root.right, key)
        elif root.val > key: root.left = self.deleteNode(root.left, key)
        return root

# @lc code=end

