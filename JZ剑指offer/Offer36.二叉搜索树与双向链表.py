"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None: return None

        stack = []
        cur = root
        last = None
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop(-1)
                if last is None: newHead = cur
                else:
                    last.right = cur
                    cur.left = last
                last = cur
                cur = cur.right
        last.right = newHead
        newHead.left = last
        return newHead
        