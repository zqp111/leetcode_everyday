#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.cur = root
        self.stack = []
        self.deeper()
        


    def next(self) -> int:
        self.cur = self.stack.pop(-1)
        nextValue = self.cur.val
        self.cur = self.cur.right
        self.deeper()
        return nextValue

    def deeper(self):
        while self.cur :
            self.stack.append(self.cur)
            self.cur = self.cur.left


    def hasNext(self) -> bool:
        return len(self.stack) >0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

