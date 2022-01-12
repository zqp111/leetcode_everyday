#
# @lc app=leetcode.cn id=2105 lang=python3
#
# [2105] 给植物浇水 II
#

# @lc code=start
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l, r = 0, len(plants)-1
        result = 0
        resA= capacityA
        resB= capacityB
        while l < r:
            if resA < plants[l]:
                if capacityA >= plants[l]:
                    result += 1
                    resA = capacityA - plants[l]
                    l +=1
            else:
                resA = resA - plants[l]
                l += 1

            if resB < plants[r]:
                if capacityB >= plants[r]:
                    result +=1
                    resB = capacityB - plants[r]
                    r -= 1
            else:
                resB = resB - plants[r]
                r -= 1
            print(l, r, result)
        if l==r:
            if resA < plants[l] and resB < plants[l]:
                return result +1
        return result
                

# @lc code=end

