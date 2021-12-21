#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        self.nums = [str(i) for i in range(1,10)]
        self.dfs(board)
        

        
    def dfs(self, board):
        m, n = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    for num in self.nums:
                        if self._canFill(board, i, j, num):
                            board[i][j] = num
                            if self.dfs(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def _canFill(self, board, i_target, j_target, num):
        for i in range(len(board)):
            if board[i][j_target] == num:
                return False
        for j in range(len(board[0])):
            if board[i_target][j] == num:
                return False
        
        k_i, v_i = divmod(i_target, 3)
        k_j, v_j = divmod(j_target, 3)
        for i in range(3):
            for j in range(3):
                if board[3*k_i+i][3*k_j+j] == num:
                    return False
        return True
# @lc code=end

