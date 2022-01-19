#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        count = dict()
        for char in s:
            count[char] = count.get(char, 0) + 1
        sortedChar = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return ''.join([char[0]*char[1] for char in sortedChar])
        
# @lc code=end

