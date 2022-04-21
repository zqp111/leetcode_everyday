#
# @lc app=leetcode.cn id=655 lang=python3
#
# [655] 输出二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:

        queue = [root]
        level_travel = []
        have_son = True
        while queue and have_son:
            cur_len = len(queue)
            level_travel.append([])
            have_son = False
            for i in range(cur_len):
                node = queue.pop(0)
                if node:
                    level_travel[-1].append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                    have_son = have_son or node.left or node.right
                else:
                    level_travel[-1].append("")
                    queue.append(None)
                    queue.append(None)

        level = len(level_travel)
        n = 2**level -1
        res = [[""]*n for _ in range(level)]
        space = 1
        for i in range(level-1, -1, -1):
            l_space = space-1
            space = 2**(level-i)
            # print(i, l_space, space)
            cur_j = l_space
            for char in level_travel[i]:
                res[i][cur_j] = char
                cur_j += space
        return res
            


# @lc code=end

