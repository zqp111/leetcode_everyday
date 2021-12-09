#
# @lc app=leetcode.cn id=1138 lang=python3
#
# [1138] 字母板上的路径
#

# @lc code=start
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ans = ""
        x_last, y_last = 0, 0
        for s in target:
            all_ = ord(s)-ord('a')
            y = all_ //5
            x = all_ % 5
            a = y-y_last
            b = x-x_last
            # print(a, b)
            y_last = y
            x_last = x

            if a > 0:
                if b > 0:
                    ans += "R"*b
                else:
                    ans += "L"*abs(b)
                ans += "D"*a
            else:
                ans += "U"*abs(a)
                if b > 0:
                    ans += "R"*b
                else:
                    ans += "L"*abs(b)
            ans += "!"
        # print(ans)
        return ans            

# @lc code=end

