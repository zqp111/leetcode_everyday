#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

    ## backtracking
    #     self.re = 0
    #     now_sum = 0
    #     coins.sort(reverse=True)
    #     # print(coins)
    #     self.backtracking(amount, coins, now_sum)
    #     return self.re
        
    # def backtracking(self, amount, coins, now_sum):
    #     if now_sum > amount:
    #         return
    #     if now_sum == amount:
    #         self.re = self.re + 1
    #         # print("now re: ", self.re)
    #         return

    #     for i, coin in enumerate(coins):
    #         now_sum += coin
    #         # print('now_sum: ', now_sum)
    #         self.backtracking(amount, coins[i:], now_sum)
    #         now_sum -= coin

    ## dp
        dp = [0]*(amount+1)
        dp[0] = 1 
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]


    ## bfs

    #     self.path = 0
    #     self.bfs(amount, coins)
    #     return self.path

    # def bfs(self, amount, coins):
    #     q = [(len(coins), amount)]

    #     while q:
    #         l, now_amount = q.pop(0)
    #         if now_amount == 0:
    #             self.path += 1
    #             continue
    #         if now_amount < 0:
    #             continue
    #         for i, coin in enumerate(coins[:l]):
    #             q.append((i+1, now_amount-coin))


# @lc code=end

