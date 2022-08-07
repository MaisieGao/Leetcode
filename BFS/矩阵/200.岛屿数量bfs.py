# from asyncio import queues
import queue
import collections
# bfs 需要queue
def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0
    n = len(grid)
    m = len(grid[0])
    island = 0

    def bfs(row, col):
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = collections.deque()
        queue.append((row,col))
        while queue:
            r,c = queue.popleft()
            for dx,dy in direction:
                x = dx+r
                y = dy+c
                #如果下一层的坐标在grid内并且是没有visit过的岛屿，queue append进去
                if 0<=x<n and 0<=y<m and grid[x][y] == '1':
                    queue.append((x,y))
                    grid[x][y] = '-1'
    
    for i in range(n):
        for j in range(m):
            #如果是岛屿，就把旁边每一层的岛屿都连在一起，练得方法是用bfs和queue
            if grid[i][j] == '1':
                bfs(i,j)
                #连在一起只加1
                island += 1
    return island
