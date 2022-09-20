def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    for i in range(len(intervals)):
        #分三种情况：
        # interval大于newInterval且无交集时
        # interval 小于newInterval且无交集时
        # 有交集时
        #if the end value is less than the start value, there is no intersection in the intervals[i]
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        #if start is larger than the intervals,then no intersection
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            #pick the smaller one of start an larger one of end
            newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
    #if can't find intervals that are larger than the end value,just append newIntervals(it means that the newInterval is at the last position)
    #只有第一个if return了，其余的都没有。如果没有return,说明newInterval最大，找不到比newInterval更大的interval,
    #所以在res append所有的intervals最后，加上newInterval
    res.append(newInterval)
    return res