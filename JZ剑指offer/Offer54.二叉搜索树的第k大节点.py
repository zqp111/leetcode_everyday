# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if root is None: return None
        stack = []
        cur = root
        index = 0
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop(-1)
                index += 1
                if index == k: return cur.val
                cur = cur.left
