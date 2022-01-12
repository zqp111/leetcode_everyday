#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        # re_dict = {}
        re = []
        stack = []
        cur_node = root
        last= float('-inf')
        is_same = False
        tmp = None
        same_num = 1
        max_same_num = 1
        while cur_node is not None or stack:
            if cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop(-1)
                if cur_node.val == last:
                    same_num += 1
                    if not is_same:
                        tmp = cur_node.val
                        is_same = True
                elif is_same:
                    if max_same_num == same_num:
                        re.append(tmp)
                    elif max_same_num < same_num:
                        re = [tmp]
                        max_same_num = same_num
                    same_num = 1
                    is_same = False
                elif not is_same and max_same_num == 1:
                    re.append(cur_node.val)
                last = cur_node.val
                cur_node = cur_node.right
        if max_same_num == same_num:
            if tmp is not None: re.append(tmp) 
        if max_same_num < same_num:
            re = [tmp]
        return re
# @lc code=end

