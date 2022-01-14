#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000': return 0
        seen = set()
        queue = ['0000']
        level = 0

        while queue:
            level += 1
            levelLen = len(queue)
            for _ in range(levelLen):
                cur = queue.pop(0)
                for node in self.__getNext(cur, seen, deadends):
                    if node == target:
                        return level
                    queue.append(node)
                seen.add(cur)
                # print(queue)
        return -1

    def __getNext(self, cur, seen, deadends):
        if cur in seen or cur in deadends: return []
        result = []
        for i in range(4):
            nowchar = int(cur[i])
            newi = nowchar + 1 if nowchar <9 else 0
            nextnode = cur[:i]+str(newi)+cur[i+1:]
            if nextnode not in seen and nextnode not in deadends:
                result.append(nextnode)
            newi = nowchar - 1 if nowchar >0 else 9
            nextnode = cur[:i]+str(newi)+cur[i+1:]
            if nextnode not in seen and nextnode not in deadends:
                result.append(nextnode)
        return result

# @lc code=end

