def updateMatrix(self, mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    m = len(mat)
    n = len(mat[0])
    queue = collections.deque()
    res = [[-1]*n for _ in range(m)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #把所有的0放进去
    #将题目转换为 0 到1的距离
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                #0到自身的距离是0
                res[i][j] = 0
                queue.append((i,j))
    #现在只剩下是1的
    while queue:
        #不需要level,所以第一个for循环不需要
        x,y = queue.popleft()
        for dx,dy in direction:
            r = x+dx
            c=y+dy
            #是邻居，在范围内并且没被走访过
            if 0<=r<m and 0<=c<n and res[r][c] == -1:
                #res加上1
                res[r][c] = res[x][y]+1
                queue.append((r,c))
    return res