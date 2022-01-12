#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = pow(2,len(nums))
        ans = []
        for i in range(N):
            tmp = []
            idx = 0
            m = i
            while m:
                if m & 1:
                    tmp.append(nums[idx])
                idx += 1
                m =m >> 1
            ans.append(tmp)
        return ans

# @lc code=end

