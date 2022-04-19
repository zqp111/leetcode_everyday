#
# @lc app=leetcode.cn id=609 lang=python3
#
# [609] 在系统中查找重复文件
#

# @lc code=start
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for path in paths:
            path = path.split(' ')
            root = path[0]
            files = path[1:]
            for file in files:
                name, content = file.split('(')
                if content[:-1] in d:
                    d[content[:-1]].append(root + '/' + name)
                else:
                    d[content[:-1]] = [root+'/'+name]
        ans = []
        for key, value in d.items():
            if len(value) > 1:
                ans.append(value)
        return ans
# @lc code=end

