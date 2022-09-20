def orangesRotting(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    queue = collections.deque()
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #将烂橘子加到queue中
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i,j))
    #set time to be -1因为最后一个橘子放进去之后time其实就已经是正确的了，要pop最后一个橘子还要加一次time,所以这个time就是多加的，所以time最开始是-1
    time = -1
    while queue:
        time += 1
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for dx, dy in direction:
                r = x+dx
                c = y+dy
                #把好橘子变成烂橘子
                #把烂橘子加进queue中
                if 0<=r<m and 0<=c<n and grid[r][c] == 1:
                    queue.append((r,c))
                    grid[r][c] = 2
    #queue完了之后还有好橘子，就return -1
    #说明好橘子怎么也够不着
    for i in range(m):
        if 1 in grid[i]:
            return -1
    #如果[0]这样的话，没有烂橘子，所以time == -1,这时候也要return 0
    if time == -1:
        return 0
    else:
        #如果有烂橘子没有好橘子，直接time = 0.因为进了一次queue. pop所有烂橘子
        #然后time += 1就变成了0
        return time
