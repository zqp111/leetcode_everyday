# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B: return False
        queue = [A]
        while queue:
            cur = queue.pop(0)
            if self.isSameTree(cur, B):
                return True
            if cur.left is not None: queue.append(cur.left)
            if cur.right is not None: queue.append(cur.right)
        return False

    def isSameTree(self, rootA, rootB):
        if rootB is None:
            return True
        if rootA is None:
            return False
        if rootA.val != rootB.val:
            return False
        return self.isSameTree(rootA.left, rootB.left) \
                and self.isSameTree(rootA.right, rootB.right)