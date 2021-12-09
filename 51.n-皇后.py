#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        tmp = []
        self.backtrace(res, n, tmp)

        res = self.convertResult(res, n)
        return res
    
    def convertResult(self, res, n):
        final_res = []
        for r in res:
            tmp = []
            for i in r:
                tmp.append('.'*i+'Q'+'.'*(n-i-1))
            final_res.append(tmp)
        return final_res


    def __can_site(self, tmp, idx):
        """[summary]

        Args:
            tmp (list[int]): 已经放置的棋子，数值代表列数
            idx (int): 将要放置第几列

        Returns:
            [type]: [description]
        """
        if idx in tmp:
            return False
        m = len(tmp) # 将要放置第几行
        for i, rol in enumerate(tmp):
            if idx == rol - (m-i) or idx == (m-i) + rol:
                return False
        return True

    
    def backtrace(self, res, n, tmp):
        if len(tmp) == n:
            res.append(tmp.copy())
            return
        
        for i in range(n):
            if self.__can_site(tmp, i):
                tmp.append(i)
                self.backtrace(res, n, tmp)
                tmp.pop()


# @lc code=end

