#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        
        for i in range(numCourses):
            visited = [0] *numCourses
            onPath = set()
            if not self.dfs(graph, i, visited, onPath): return False
        return True

    def dfs(self, graph, node, visited, onPath:set()):
        if visited[node]: return True
        
        visited[node] = True
        onPath.add(node)
        for curNeighbor in graph[node]:
            if curNeighbor in onPath: return False
            if not self.dfs(graph, curNeighbor, visited, onPath):
                return False
        onPath.remove(node)
        return True

# @lc code=end

