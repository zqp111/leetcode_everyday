# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.travel(root, p, q)

    def travel(self, node, p, q):
        if node is p or node is q: return node
        if node is None: return None

        l = self.travel(node.left, p, q)
        r = self.travel(node.right, p, q)
        if l is not None and r is not None: return node
        if l is None: return r
        return l