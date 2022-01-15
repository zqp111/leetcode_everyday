# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if root is None: return []

        self.result = []
        self.travel(root, [], 0, target)
        return self.result


    def travel(self, node, tmp, tmpSum, target):
        if node.left is None and node.right is None: # 叶子节点
            tmp.append(node.val)
            tmpSum += node.val
            if tmpSum == target: 
                self.result.append(tmp.copy())
            tmp.pop(-1)
            tmpSum -= node.val
            return
        
        tmp.append(node.val)
        tmpSum += node.val
        if node.left is not None: self.travel(node.left, tmp, tmpSum, target)
        if node.right is not None: self.travel(node.right, tmp, tmpSum, target)
        tmp.pop(-1)
        tmpSum -= node.val