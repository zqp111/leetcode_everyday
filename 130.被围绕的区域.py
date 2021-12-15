#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for i in range(len(board)):
            self.dfs(board, i, 0)
            self.dfs(board, i, len(board[0])-1)
        
        for j in range(len(board[0])):
            self.dfs(board, 0, j)
            self.dfs(board, len(board)-1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == "R":
                    board[i][j] = "O"


    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >=len(board) or j >= len(board[0]):
            return 
        if board[i][j] == "O":
            board[i][j] = "R"
            self.dfs(board, i+1, j)
            self.dfs(board, i-1, j)
            self.dfs(board, i, j+1)
            self.dfs(board, i, j-1)
    
# @lc code=end

