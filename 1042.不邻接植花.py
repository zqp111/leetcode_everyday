#
# @lc app=leetcode.cn id=1042 lang=python3
#
# [1042] 不邻接植花
#

# @lc code=start
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        graph = self.buildGraph(n, paths)
        # print(graph)
        result = [0] * n
        for i in range(n):
            # print(result)
            if result[i] == 0:
                stack = [i]
                while stack:
                    # print('in:', i, result)
                    cur = stack.pop(-1)
                    result[cur] = self.getColor(graph, cur, result)
                    for ner in graph[i]:
                        if not result[ner]: stack.append(ner)
        return result

    def getColor(self, graph, i, result):
        ner = [result[index] for index in graph[i]]
        for color in range(1, 5):
            if color not in ner:
                return color
            
        
    def buildGraph(self, n, paths):
        graph = [[] for _ in range(n)]
        for path in paths:
            graph[path[0] -1].append(path[1] -1)
            graph[path[1] -1].append(path[0] -1)
        return graph

# @lc code=end

