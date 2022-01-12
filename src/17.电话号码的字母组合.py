#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numDict = {'2': 'abc', '3': 'def',
                '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs',
                '8': 'tuv', '9': 'wxyz'}   
        result = []
        self.backtracking(digits, 0, '', result, numDict)
        return result

    def backtracking(self, digits, index, tmp, result, numDict):
        # print(index, len(digits))
        if index >= len(digits):
            result.append(tmp)
            return
        for char in numDict[digits[index]]:
            tmp += char
            self.backtracking(digits, index+1, tmp, result, numDict)
            tmp = tmp[:-1]
# @lc code=end

