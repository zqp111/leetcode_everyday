# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        if root is not None:
            queue.append(root)
        result = []
        left = False
        while queue:
            levelLen = len(queue)
            tmp = []
            left = not left
            for _ in range(levelLen):
                cur = queue.pop(0)
                if left :
                    tmp.append(cur.val)
                else:
                    tmp.insert(0, cur.val)
                if cur.left is not None: queue.append(cur.left)
                if cur.right is not None: queue.append(cur.right)
            result.append(tmp.copy())
        return result