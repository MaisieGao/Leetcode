def numIslands(self, grid: List[List[str]]) -> int:
    
    res = 0
    m = len(grid)
    n = len(grid[0])
    #如果是1，淹了它（把他变成0），并且确保它上下左右的1都被淹了
    def dfs(x, y):
        grid[x][y] = '0'
        for dx,dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                dfs(nx, ny)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                res += 1
                # 淹没包含这个陆地的整个岛屿
                dfs(i,j) 
    return res