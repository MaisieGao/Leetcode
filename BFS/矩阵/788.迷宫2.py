def shortestDistance(self, maze, start, destination):
    import heapq
    if not start or not destination:
        return -1
    row_end, col_end = len(maze) - 1, len(maze[0]) - 1
    seen = set()
    queue = [(0, start[0], start[1])]
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while len(queue):
        (distance, current_x, current_y) = heapq.heappop(queue)
        if (current_x, current_y) not in seen:
            if current_x == destination[0] and current_y == destination[1]:
                return distance
            seen.add((current_x, current_y))
            for (dx, dy) in directions:
                x, y, d = current_x, current_y, distance
                                    # roll until out of boundary or reach wall
                while x >= 0 and x <= row_end and y >= 0 and y <= col_end and maze[x][y] != 1:
                    x += dx
                    y += dy
                    d += 1
                                    # back to previous legal position
                x -= dx
                y -= dy
                d -= 1
                                     # add point to pq sorted by distance
                heapq.heappush(queue, (d, x, y))
    return -1