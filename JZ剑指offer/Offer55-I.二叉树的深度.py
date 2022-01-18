# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            levelLen = len(queue)
            for _ in range(levelLen):
                cur = queue.pop(0)
                if cur.left is not None: queue.append(cur.left)
                if cur.right is not None: queue.append(cur.right)
        return depth