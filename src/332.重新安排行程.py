#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start
# import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        transforDict = dict()
        for s, e in tickets:
            if not transforDict.__contains__(s):
                transforDict[s] = [e]
            else:
                transforDict[s].append(e)
        for k, v in transforDict.items():
            transforDict[k] = sorted(v)
        cur = 'JFK'
        return self.dfs(transforDict, cur, [])

    def __is_empty(self, dic):
        for k, v in dic.items():
            if v:
                return False
        return True

    def dfs(self, transforDict, cur, path):
        print(cur)
        if not transforDict.__contains__(cur):
            if self.__is_empty(transforDict):
                path.append(cur)
                return path
            else:
                return None
        if not transforDict[cur]:
            if self.__is_empty(transforDict):
                path.append(cur)
                return path
            else:
                return None
        
        path.append(cur)
        
        for i in range(0, len(transforDict[cur])):
            next_ = transforDict[cur].pop(i)
            rpath = self.dfs(transforDict, next_, path)
            if rpath:
                return rpath
            
            transforDict[cur].insert(i, next_)
        path.pop(-1)
        return None

            
# @lc code=end

