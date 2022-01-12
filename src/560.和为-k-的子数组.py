#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumArray = []
        tmpSum = 0
        for num in nums:
            tmpSum += num
            sumArray.append(tmpSum)
        
        result = 0
        seen = dict()
        for sumNum in sumArray:
            if sumNum == k: result += 1
            if seen.get(sumNum, None) is not None:
                result += seen[sumNum]
            seen[k+sumNum] = seen.get(k+sumNum, 0) + 1
            # print(seen, result)
        return result

# @lc code=end

