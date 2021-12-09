#
# @lc app=leetcode.cn id=928 lang=python3
#
# [928] 尽量减少恶意软件的传播 II
#

# @lc code=start
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        import numpy as np
        # print(graph)

        graph = np.array(graph, dtype=np.bool)
        # print(graph)
        init = np.array([[1 if i in initial else 0 for i in range(len(graph))]], dtype=np.bool)

        min_node = len(graph)
        # print(init)
        droup_index = 0

        for i in range(len(graph)) :
            tmp_h = graph[i, :].copy()
            tmp_c = graph[:, i].copy()
            graph[i, :] = 0
            graph[:, i] = 0
            tmp = init[0, i]
            init[0, i] = 0
            # print('init', init)
            # print('graph', graph)
            # print('h', tmp_h)
            # print('c', tmp_c)
            last_node = init
            new_node = np.matmul(last_node, graph)
            nodes = np.sum(new_node)
            # print(i, new_node)
            if nodes < min_node:
                droup_index = i
                min_node = nodes

            while (new_node != last_node).any():
                last_node = new_node
                new_node = np.matmul(last_node, graph)
                nodes = np.sum(new_node)
                # print(i, new_node)
                if nodes < min_node:
                    droup_index = i
                    min_node = nodes
            graph[i, :] = tmp_h
            graph[:, i] = tmp_c
            init[0, i] = tmp
            
        return droup_index
# @lc code=end

