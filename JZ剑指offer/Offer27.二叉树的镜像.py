# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        return self.reverse(root)

    def reverse(self, node):
        if node is None: return None
        newleft = self.reverse(node.right)
        newright = self.reverse(node.left)
        node.left = newleft
        node.right = newright
        return node