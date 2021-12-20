#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        for i in range(len(people)):
            if people[i][1] != i:
                people.insert(people[i][1], people.pop(i))
        return people
# @lc code=end

