# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        queue = []
        if root is not None:
            queue.append(root)
        result = []
        while queue:
            cur = queue.pop(0)
            result.append(cur.val)
            if cur.left is not None: queue.append(cur.left)
            if cur.right is not None: queue.append(cur.right)
        return result
