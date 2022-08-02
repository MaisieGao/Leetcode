class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the intervals by the first number
        #[[1,2],[3,4],[3,5]] - key是[1,2], i[0] = 1
        intervals.sort(key = lambda i : i[0])
        #
        output = [intervals[0]]
        for start, end in intervals[1:]:
            #上一个结束是Output的最后一个sublist的第二个值
            lastEnd = output[-1][1]
            #如果这次的start比上个值的end要小，比如【【1,5】，【2,4】】中2小于5
            #我们要修改上一个sublist里end的值，相当于合并【【1,5】】,为了防止出现这种5>4的情况，我们需要保留5，所以我们比较上一个的end和这一个end谁大就保留谁
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            #如果没有重叠部分，就把这个区间加进output中
            else:
                output.append([start,end])
        return output