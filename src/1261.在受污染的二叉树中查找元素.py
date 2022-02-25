#
# @lc app=leetcode.cn id=1261 lang=python3
#
# [1261] 在受污染的二叉树中查找元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        if self.root is None: return False

        path = []
        while target != 0:
            if target % 2 == 0:
                target = (target -2) //2
                path.insert(0, 1)
            else:
                target = (target -1) //2
                path.insert(0, 0)
        
        curNode = self.root
        for p in path:
            if p == 0 :
                if curNode.left is None: return False
                curNode = curNode.left
            else:
                if curNode.right is None: return False
                curNode = curNode.right
        return True
                



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end

