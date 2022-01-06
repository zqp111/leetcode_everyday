#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        pathStack = []
        tmp = ''
        for i in range(len(path)):
            if path[i] == '/':
                if tmp:
                    if tmp == '..' : 
                        if pathStack:
                            pathStack.pop(-1)
                    elif tmp == '.': pass
                    else: pathStack.append(tmp)
                tmp = ''
            else: tmp += path[i]
        if tmp:
            if tmp == '..': 
                if pathStack:
                    pathStack.pop(-1)
            elif tmp == '.': pass
            else: pathStack.append(tmp)

        # print(pathStack)
        result = ''
        for path in pathStack:
            result = result + '/' + path
        return result if result else '/'


# @lc code=end

