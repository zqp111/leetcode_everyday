#
# @lc app=leetcode.cn id=1487 lang=python3
#
# [1487] 保证文件名唯一
#

# @lc code=start
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = {}
        ans = []
        for name in names:
            if name in seen:
                seen[name] += 1
                newName = name + '(' + str(seen[name]) + ')'
                while newName in seen:
                    seen[name] += 1
                    newName = name + '(' + str(seen[name]) + ')'
            else:
                newName = name
            
            ans.append(newName)
            seen[newName] = 0
        return ans
# @lc code=end

