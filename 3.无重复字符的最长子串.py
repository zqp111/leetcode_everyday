#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0
        max_ = 0
        for i, c in enumerate(s):
            if N-i < max_:
                return max_
            b = s[i]
            tmp = 1
            for j in range(i+1, N):
                if s[j] in b:
                    break
                tmp += 1
                b += s[j]
            max_ = max(max_, tmp)
        return 1


# @lc code=end

