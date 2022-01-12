#
# @lc app=leetcode.cn id=467 lang=python3
#
# [467] 环绕字符串中唯一的子字符串
#

# @lc code=start
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if len(p) == 0:
            return 0
        pre = 1
        ans = 1
        nums = [0]*26
        nums[ord(p[0])-ord('a')]=1

        for i in range(1, len(p), 1):
            if ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i]) - ord(p[i-1]) == -25 :
                pre += 1
            else :
                pre = 1
            nums[ord(p[i])-ord('a')] = max(nums[ord(p[i])-ord('a')], pre)
        return sum(nums)
# @lc code=end

