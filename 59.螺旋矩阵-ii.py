#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        # import numpy as np

        # map = np.zeros((n, n), dtype=np.int32)
        # cycle_num = n // 2 + 1
        # start, end = 1, 1
        # for i in range(cycle_num):
        #     end += (n-i*2)
        #     map[i, i:n-i] = list(range(start, end))
        #     start = end

        #     if end == n**2:
        #         break

        #     end += (n-i*2-1) 
        #     map[i+1:n-i, n-1-i] = list(range(start, end))
        #     start = end


        #     end += (n-i*2-1)
        #     map[n-1-i, i:n-(i+1)] = list(range(end-1, start-1, -1))
        #     start = end
            
        #     end += (n-i*2-2)
        #     map[i+1:n-(i+1), i] = list(range(end-1, start-1, -1))
        #     start = end

        # return map.tolist()


        state = 1
        ans = [[0]*n for _ in range(n)]
        ans[0][0] = 1
        i, j = 0, 0
        tmp = 1
        
        while tmp<n**2:
            # print(i, j, tmp, state, ans)
            if state == 1:
                if j < n-1 and ans[i][j+1] == 0:
                    j += 1
                    tmp += 1
                    ans[i][j] = tmp
                    if j == n-1:
                        state = 2
                else:
                    state = 2

            elif state == 2:
                if i < n-1 and ans[i+1][j] == 0:
                    i += 1
                    tmp += 1
                    ans[i][j] = tmp
                    if i == n-1:
                        state = 3
                else:
                    state = 3
            elif state == 3:
                if j > 0 and ans[i][j-1] == 0:
                    j -= 1
                    tmp += 1
                    ans[i][j] = tmp
                    if j == 0:
                        state = 4
                else:
                    state = 4
            elif state == 4:
                if i > 0 and ans[i-1][j] == 0:
                    i -= 1
                    tmp += 1
                    ans[i][j] = tmp
                else:
                    state = 1
        return ans
# @lc code=end

