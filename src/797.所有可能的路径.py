#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        self.dfs(graph, 0, len(graph)-1, [], result)
        return result


    def dfs(self, graph, node, target, pathTmp, result):
        if node == target:
            pathTmp.append(node)
            result.append(pathTmp.copy())
            pathTmp.pop(-1)
            return 
        
        pathTmp.append(node)
        for i in range(len(graph[node])) :
            self.dfs(graph, graph[node][i], target, pathTmp, result)
        pathTmp.pop(-1)
# @lc code=end

