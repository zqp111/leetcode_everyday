#
# @lc app=leetcode.cn id=1819 lang=python3
#
# [1819] 序列中不同最大公约数的数目
#

# @lc code=start
import math
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        ## backtracking 超时
    #     maxGcds = set()
    #     self.backtracking(nums, [], [], maxGcds)
    #     return len(maxGcds)

    # def backtracking(self, nums, tmp:list, curGcds:list, maxGcds:set):
    #     # print(nums, maxGcds, tmp, curGcds)
    #     if curGcds and curGcds[-1] not in maxGcds:
    #         maxGcds.add(curGcds[-1])
    #     if len(nums) == 0: 
    #         return

    #     if curGcds and curGcds[-1] == 1: # 剪枝
    #         if 1 not in maxGcds:
    #             maxGcds.add(1)
    #         return

    #     for i in range(len(nums)):
    #         if nums[i] not in nums[:i] and nums[i] not in tmp: # 剪枝，不选择相同的数值
    #             tmp.append(nums[i])
    #             gcdTmp = curGcds.copy()
    #             self.addgcd(curGcds, nums[i])
    #             self.backtracking(nums[i+1:], tmp, curGcds, maxGcds)
    #             curGcds = gcdTmp.copy()
    #             tmp.pop(-1)
    
    # def addgcd(self, gcds, nums):
    #     if not len(gcds):
    #         r =[]
    #         sqrtNum = int(math.sqrt(nums))
    #         for i in range(1, sqrtNum+1):
    #             a, b = divmod(nums, i)
    #             if not b: 
    #                 gcds.append(i)
    #                 if i != a: r.insert(0, a)
    #         # print('add:',gcds , r)
    #         gcds += r
    #     else:
    #         index = len(gcds) -1
    #         while index >= 0:
    #             if nums % gcds[index]:
    #                 gcds.pop(index)
    #             index -=1          
                
        nums = set(nums)
        c = max(nums)
        ans = 0

        for y in range(1, c + 1):
            g = None
            for x in range(y, c + 1, y):
                if x in nums:
                    if not g:
                        g = x
                    else:
                        g = math.gcd(g, x)
                    if g == y:
                        ans += 1
                        break
        return ans

# @lc code=end

