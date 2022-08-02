#we need to sort so O(n log n)
#飞机题和这个题是完全一样的
def min_meeting_rooms(self, intervals: List[Interval]) -> int:
    # Write your code here
    #建立两个sorted array
    #start = [0,5,10]
    #end = [10,15,30]
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])
    #两个pointer分别是start和end里的
    s, e = 0,0
    res = 0
    count = 0
    #假如start里的元素小于end里面的元素，说明有一个meeting start, count+1
    #move to the next start index
    #假如end小于等于start里的元素，说明这个meeting end了，count-1. 
    #move to the next end Index
    while s < len(intervals):
        if start[s] < end[e]: 
            s+=1
            count+=1
        else:
            e+=1
            count-=1
        res = max(res, count)
    return res

