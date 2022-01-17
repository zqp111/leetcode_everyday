#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inAngle, outAngle = [0]*n, [0]*n
        for i in range(len(trust)):
            inAngle[trust[i][1]-1] += 1
            outAngle[trust[i][0]-1] += 1
        
        person = []

        for i in range(n):
            if inAngle[i] == n-1 and outAngle[i] == 0:
                person.append(i+1)
        if len(person) == 1:
            return person[0]
        return -1
# @lc code=end

