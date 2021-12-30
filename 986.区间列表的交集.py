#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):

            ## 空集
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif firstList[i][0] > secondList[j][1]:
                j += 1
            
            ## 有交集
            elif firstList[i][1] > secondList[j][1]:
                result.append([max(firstList[i][0], secondList[j][0]), secondList[j][1]])
                j += 1
            
            elif firstList[i][1] <= secondList[j][1]:
                result.append([max(firstList[i][0], secondList[j][0]), firstList[i][1]])
                i += 1 #
        return result

# @lc code=end

