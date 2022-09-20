class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        #两个指针
        i, j = 0,0
        #当两个interval都有值的时候
        while i < len(firstList) and j < len(secondList):
            #交集是取大的那个开始和小的那个结束
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1],secondList[j][1])
            #如果start < end,表示有交集
            if start <= end:
                res.append([start,end])
            #我们还要让i和j往前走
            #如果说第一个array的end小于第二个array的end,我们让第一个array往前移一个
            if firstList[i][1] < secondList[j][1]:
                i += 1
            #如果说第一个array的end大于第二个array的end
            else:
                j += 1
        return res
