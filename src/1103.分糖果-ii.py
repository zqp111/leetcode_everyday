#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i = 1
        ans = [0]*num_people
        while True:
            if i < candies:
                ans[(i-1)%num_people] += i
            else:
                break
            candies -= i
            i += 1
        ans[(i-1)%num_people] += candies
        return ans

# @lc code=end

