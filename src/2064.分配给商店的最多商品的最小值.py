#
# @lc app=leetcode.cn id=2064 lang=python3
#
# [2064] 分配给商店的最多商品的最小值
#

# @lc code=start
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        ## dp 超时
    #     dp = [[float('inf')]*n for i in range(len(quantities))]
    #     for i in range(n):
    #         dp[-1][i] = self.getNum(quantities[-1], i+1)
    #         # num, d = divmod(quantities[-1], i+1)
    #         # dp[-1][i] = num if d == 0 else num+1
        
    #     for i in range(len(quantities)-2, -1, -1):
    #         for j in range(len(quantities)-1-i, n):
    #             for k in range(j-1, -1, -1):
    #                 if dp[i+1][k] == float('inf'): break
    #                 dp[i][j] = min(dp[i][j], max(dp[i+1][k], self.getNum(quantities[i], j-k)))
    #     # print(dp)
    #     return dp[0][-1]

    # def getNum(self, quantity, num):
    #     num, d = divmod(quantity, num)
    #     return num if d == 0 else num+1

    # 判定问题
        def check(x: int) -> bool:
            # 计算所需商店数量的最小值，并与商店数量进行比较
            cnt = 0
            for q in quantities:
                cnt += (q - 1) // x + 1
            return cnt <= n
        
        l, r = 1, max(quantities) + 1
        # 二分查找寻找最小的使得判定问题为真的 x
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l

# @lc code=end

