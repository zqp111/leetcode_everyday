# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return False if self.travel(root) == -1 else True
    
    def travel(self, root):
        if root is None:
            return 0
        l = self.travel(root.left)
        r = self.travel(root.right)
        if l == -1 or r == -1:
            return -1
        if l - r > 1 or l - r < -1:
            return -1
        return max(l, r)+1

        