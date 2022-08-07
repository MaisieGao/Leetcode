def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj = collections.defaultdict(list)
    indegree = collections.defaultdict(int)
    res = []
    for a, b in prerequisites:
        adj[b].append(a)
        indegree[a] += 1
    queue=collections.deque()
    for k in range(numCourses):
        if indegree[k] == 0:
            queue.append(k)
    while queue:
        node = queue.popleft()
        res.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(res) == numCourses:
        return res
    else:
        return []
