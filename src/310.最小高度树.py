#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    #     if n <= 2: return [[0], [0, 1]][n-1]
    #     depth = [float('inf')]*n

    #     linked = [[] for _ in range(n)]
    #     for edge in edges:
    #         linked[edge[0]].append(edge[1])
    #         linked[edge[1]].append(edge[0])
        
    #     for i in range(n):
    #         if len(linked[i]) == 1:
    #             depth[i] = 0
    #             self.dfs(depth, i, linked, set())
    #     maxdepth = max(depth)
    #     result = []
    #     for i in range(n):
    #         if depth[i] == maxdepth:
    #             result.append(i)
    #     return result
    
    # def dfs(self, depth, i, linked, path):
    #     path.add(i)
    #     for node in linked[i]:
    #         depth[node] = min(depth[node], depth[i]+1)
    #         if node not in path:
    #             self.dfs(depth, node, linked, path)

        res = []
        if n==1:
            res.append(0)
            return res
        degree = [0]*n #记录每个点的度
        map = defaultdict(list) #存储邻居节点
        # 初始化每个节点的度和邻居
        for edge in edges:
            degree[edge[0]]+=1
            degree[edge[1]]+=1
            map[edge[0]].append(edge[1])
            map[edge[1]].append(edge[0])
        
        # 记录度为1的叶子节点
        queue = deque()
        for i in range(n):
            if degree[i]==1:
                queue.append(i)
        
        #每次遍历叶子节点，每一轮将叶子节点从树上删除后将新的叶子节点入队进行下一轮遍历
        while len(queue)>0:
            res = []
            size = len(queue)
            # 遍历叶子节点
            for i in range(size):
                cur = queue.pop()
                res.append(cur)
                neighbors = map[cur]
                for neighbor in neighbors:
                    # 将叶子节点的邻居节点的度减一，若是新的叶子节点，则入队
                    degree[neighbor]-=1
                    if degree[neighbor]==1:
                        queue.appendleft(neighbor)
        # 返回最后一轮的叶子节点，就是最小高度树的根节点
        return res

# @lc code=end

