#
# @lc app=leetcode.cn id=1769 lang=python3
#
# [1769] 移动所有球到每个盒子所需的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        dp = [0] * n
        left = right = 0

        # init
        for i in range(n): 
            if boxes[i] == '1':
                dp[0] += i
                right += 1
        
        for j in range(1, n):
            if boxes[j-1] == '1':
                left += 1
                right -= 1
            dp[j] = dp[j-1] - right + left

        return dp
        
# @lc code=end

