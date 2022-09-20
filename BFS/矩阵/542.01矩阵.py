def updateMatrix(self, mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    n = len(mat)
    m = len(mat[0])
    queue = collections.deque()
    res = [[-1]*m for _ in range(n)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #把所有的0放进去
    #将题目转换为 0 到1的距离
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                #0到自身的距离是0
                res[i][j] = 0
                queue.append((i,j))
    #现在只剩下是1的
    while queue:
        #不需要level,所以第一个for循环不需要
            r, c = queue.popleft()
            for dx, dy in direction:
                x = dx+r
                y = dy+c
            #是邻居，在范围内并且没被走访过
            if 0<=x<n and 0<=y<m and res[x][y] == -1:
                #res加上1
                res[x][y] = 1 + res[r][c]
                queue.append((x,y))
    return res