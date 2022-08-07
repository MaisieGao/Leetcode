def maxDistance(self, grid: List[List[int]]) -> int:
    distance = -1
    n = len(grid)
    queue = collections.deque()
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #如果是海岛，将他append进去
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i,j))
    #如果全是海岛或者陆地，返回-1
    if len(queue) ==0 or len(queue) == n*n:
        return -1
    while queue:
        #层数+1（可以得到最大层数）
        distance += 1
        #每一层用一个for循环，Pop所有此层的值
        for _ in range(len(queue)):
            x, y = queue.popleft()
            #上下左右是下一层，得到新的坐标
            for dx, dy in direction:
                nx = x+dx
                ny = y+dy
                #如果新的坐标在grid内并且是陆地
                if 0<=nx<n and 0<=ny<n and grid[nx][ny] == 0:
                    #将其append到queue中
                    queue.append((nx,ny))
                    #mark as visited，为了不重复append
                    #不是双等号
                    grid[nx][ny] = -1
    return distance
