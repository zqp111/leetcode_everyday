class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [0, -prices[0]]
        for i in range(len(prices)):
            dp[0] = max(dp[0], dp[1]+prices[i])
            dp[1] = max(dp[1], -prices[i])
        return dp[0]
