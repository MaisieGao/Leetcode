# Definition of Interval:
# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
# """

# class Solution:
#     """
#     @param intervals: an array of meeting time intervals
#     @return: if a person could attend all meetings
#     """
def can_attend_meetings(self, intervals: List[Interval]) -> bool:
    #首先sort intervals
    intervals.sort(key = lambda i : i.start)
    #然后有两个值：分别是前一个和后一个。前一个的end > 后一个的start的情况下，二者有重合，return false
    #otherwise, return true
    for i in range(1,len(intervals)):
        pre = intervals[i-1]
        cur = intervals[i]
        if cur.start <= pre.end:
            return False
    return True
