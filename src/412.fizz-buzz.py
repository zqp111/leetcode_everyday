#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            tmp =""
            if i%3 == 0:
                tmp += 'Fizz'
            if i%5 == 0:
                tmp += 'Buzz'
            if tmp == '':
                tmp += str(i)
            ans.append(tmp)
        return ans
# @lc code=end

