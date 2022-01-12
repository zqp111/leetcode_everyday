#
# @lc app=leetcode.cn id=939 lang=python3
#
# [939] 最小面积矩形
#

# @lc code=start
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # points.sort() # 升序
        # grid_map = {}
        # for x, y in points:
        #     if x not in grid_map.keys():
        #         grid_map[x] = [y]
        #     grid_map[x].append(y)
        
        # minimum_area = float('inf')


        # for x in sorted(grid_map.keys()):
        #     y_list = sorted(grid_map[x])
        #     if len(y_list) < 2:
        #         continue
        #     for y in y_list:
                
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            if len(column) < 2:
                continue
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j-1, -1, -1):
                    y1 = column[i]
                    if y2-y1 > ans:
                        break
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0
        
        


# @lc code=end

