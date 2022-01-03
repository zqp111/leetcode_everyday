# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        left, right = [], []
        if root is None: return True
        if root.left is None and root.right is None: return True
        if root.left is None or root.right is None: return False

        left.append(root.left)
        right.append(root.right)
        while left and right:
            l, r = left.pop(0), right.pop(0)
            if l.val != r.val: return False

            if l.left is not None and r.right is not None:
                left.append(l.left)
                right.append(r.right)
            elif l.left is not None or r.right is not None:
                return False
            if l.right is not None and r.left is not None:
                left.append(l.right)
                right.append(r.left)
            elif l.right is not None or r.left is not None:
                return False
        return True