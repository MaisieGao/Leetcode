class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        #change boarder "o" into "T" and connected "o" into "T"
        def dfs(r,c):
            if (r <0 or c < 0 or r>=m or c>=n or board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        #change boarder "o" into "T" 
        for i in range(m):
            for j in range(n):
                if ((i in [0,m-1] or j in [0,n-1]) and board[i][j] == 'O'):
                    dfs(i,j)

        #change other o into x
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        #change t into O
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'

