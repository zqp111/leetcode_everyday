#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        a = list(S)
        left, right = 0, len(a)-1
        while left < right:
            if not a[left].isalpha():
                left += 1
            elif not a[right].isalpha():
                right -= 1
            else:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
        return ''.join(a)


# @lc code=end

