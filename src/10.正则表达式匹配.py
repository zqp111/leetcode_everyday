#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        split = self.splitP(p)
        # print(split)
        dp = [[False]*(len(s)+1) for _ in range(len(split)+1)]
        dp[0][0] = True
        for i in range(1, len(split)+1):
            if len(split[i-1]) == 2:
                dp[i][0] = dp[i-1][0]
        
        for i in range(1, len(split)+1):
            for j in range(1, len(s)+1): 
                if len(split[i-1]) == 1:
                    # print(split[i-1], s[j-1])
                    dp[i][j] = ((split[i-1] == '.' or split[i-1] == s[j-1])) and dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j] or ((split[i-1][0] == '.' or split[i-1][0] == s[j-1]) and dp[i][j-1]) 
        # print(dp)
        return dp[-1][-1]



    def splitP(self, p): 
        index = 0
        splited = []
        while index < len(p)-1:
            if p[index]!= '*':
                if p[index+1]=='*':
                    splited.append(p[index:index+2])
                    index += 2
                else:
                    splited.append(p[index:index+1])
                    index += 1
        if p[-1] != '*': splited.append(p[-1])
        return splited

# @lc code=end

