def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # write your code here
        if not maze:
            return False
        m = len(maze)
        n = len(maze[0])
        visit = set()
        queue = collections.deque()
        #加上第一个球的位置
        queue.append((start[0], start[1]))
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            #pop之后，把位置加到visit里面
            #pop的点其实是start的点
            x, y = queue.popleft()
            visit.add((x,y))
            #如果pop的x,y正好是destination，那肯定return True
            if (x,y) == (destination[0], destination[1]):
                return True
            for dx,dy in direction:
                xx, yy = x, y
                while 0 <= xx + dx < len(maze) and 0 <= yy + dy < len(maze[0]) and maze[xx+dx][yy+dy] == 0:
                    xx, yy = xx + dx, yy + dy
                if maze[xx][yy] == 0 and (xx, yy) not in visit:
                    queue.append((xx,yy))
        return False