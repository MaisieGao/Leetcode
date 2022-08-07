def floodFill(self, image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """
    m = len(image)
    n = len(image[0])
    #找出现在这个点的颜色
    target = image[sr][sc]
    #如果染的颜色就是现在的颜色，就不用染了
    if target == color:
        return image
    queue = collections.deque()
    #把这个点放进queue
    queue.append((sr,sc))
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x,y = queue.popleft()
        #把这个点的新颜色变成color
        image[x][y] = color
        for dx,dy in direction:
            r = x+dx
            c = y+dy
            #新的点如果和原来的颜色是一样的，又是邻居
            #就把他放进queue里（这样下一次就能染成新的颜色）
            if 0<=r<m and 0<=c<n and image[r][c] == target:
                queue.append((r,c))
    return image