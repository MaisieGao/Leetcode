def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #邻接表和indegree表是两个hashmap
    #hashmap中的value的类型adj是list,因为b可能对应好多
    #indegree的value是int,因为代表有多少个indegree
    adj = collections.defaultdict(list)
    indegree = collections.defaultdict(int)
    res = []

    for a,b in prerequisites:
        #1.用prerequisite创立邻接表
        #b是要先修的课程，所以是b:a
        adj[b].append(a)
        #不是adj[b] = a,因为adj[b]是一个list,里面可能有好多elements,如果
        #等于a的话就成了【a】，变成只有一个element了
        #用prerequisite创立Indegree表
        #如果有a有必须先修的课程，a的入度+1
        indegree[a] += 1
    #建立队列，入度为0的点进入队列
    #k从0开始，代表从第0个课开始
    queue = collections.deque()
    for k in range(numCourses):
        #课0没有indegree,就把他放进queue中
        #queue里面专门放indegree是0的课（没有了prerequisite的课）
        if indegree[k] == 0:
            queue.append(k)
    while queue:
        classes = queue.popleft()
        res.append(classes)
        #课0的邻居的indegree会减1
        for neighbor in adj[classes]:
            indegree[neighbor] -= 1
            #如果邻居的indegree因此变成0，我们把他加进queue中
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    #假如res的数量不是numCourses的数量，说明有些课没有进queue,说明他们的indegree不是0.说明其中有环
    #【0,1】和【1,0】会导致0和1的indegree都不是0
    return len(res) == numCourses

    [b:[a,c]]
    去掉b，有【a,c】
    a的indegree-1 = 0
    c的indegree-1 = 0
    indegree == 0就加到queue里，说明是下一个，然后pop出去