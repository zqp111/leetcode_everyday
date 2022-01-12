#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        re = []

        saved_re = [[-1]*len(heights[0]) for _ in range(len(heights))]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                status = self.dfs(heights, i, j, float('inf'), saved_re)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                status = self.dfs(heights, i, j, float('inf'), saved_re)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                status = self.dfs(heights, i, j, float('inf'), saved_re)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                status = self.dfs(heights, i, j, float('inf'), saved_re)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                status = self.dfs(heights, i, j, float('inf'), saved_re)
                if status == 3:
                    re.append([i, j])
                # max_length = max(max_length, self.dfs(heights, i, j, float('-inf'), saved_re))
        # self.dfs(heights, 0, 0, float('inf'), saved_re)
        # print(saved_re)
        return re

    def dfs(self, heights, i, j, last, saved_re):
        # print(i, j, last, saved_re)
        if i < 0 or j < 0 :
            return 1
        if i >=len(heights) or j >= len(heights[0]):
            return 2
        if heights[i][j] > last:
            return 0
        else:
            if (saved_re[i][j] != -1 and last != float('inf')) or (saved_re[i][j] == 3):
                return saved_re[i][j]
            saved_re[i][j] = 0
            last = heights[i][j]
            saved_re[i][j] |= self.dfs(heights, i+1, j, last, saved_re)
            saved_re[i][j] |= self.dfs(heights, i-1, j, last, saved_re)
            saved_re[i][j] |= self.dfs(heights, i, j+1, last, saved_re)
            saved_re[i][j] |= self.dfs(heights, i, j-1, last, saved_re)
            return saved_re[i][j]
# @lc code=end

