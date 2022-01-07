class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        dp = [1] * (len(num)+1)
        for i in range(len(num)-2, -1, -1):
            dp[i] = dp[i+1]
            if num[i]!='0' and int(num[i:i+2]) < 26:
                dp[i] += dp[i+2]
        return dp[0]