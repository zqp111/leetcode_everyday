#
# @lc app=leetcode.cn id=1609 lang=python3
#
# [1609] 奇偶树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = []
        if root is not None:
            queue.append(root)
        level = 0
        while queue:
            levelLen =  len(queue)
            if level%2 == 0:
                last = float('-inf')
            else:
                last = float('inf')
            for _ in range(levelLen):
                curNode = queue.pop(0)
                if (level%2 == 0 and curNode.val <= last) or \
                    (level%2 == 1 and curNode.val >= last) :
                    return False
                if curNode.val %2 == level%2: return False
                last = curNode.val
                if curNode.left: queue.append(curNode.left)
                if curNode.right: queue.append(curNode.right)
            level += 1
        return True
# @lc code=end

