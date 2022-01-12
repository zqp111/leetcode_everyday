#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = self.get_state(i, j, board)
        
        # print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0

    
    def get_state(self, i, j, board):
        tmp = 0
        for index_i in range(max(0, i-1), min(len(board), i+2)):
            for index_j in range(max(0, j-1), min(len(board[0]), j+2)):
                if index_j == j and index_i == i:
                    continue
                if board[index_i][index_j] == 1 or board[index_i][index_j] == -1:
                    tmp += 1
        # print(tmp, max(0, i-1), min(len(board), i+2), max(0, j-1), min(len(board[0]), j+2))
        if board[i][j]:
            if tmp < 2 or tmp >= 4:
                return -1
            return 1
        else:
            if tmp == 3:
                return 2
            return 0
# @lc code=end

