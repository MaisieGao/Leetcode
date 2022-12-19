class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #看有没有全局变量
        path = []
        res = []
        #递归函数参数返回值
        #貌似是每个node都要return,不是在中止条件里return
        #startIndex 因为是组合
        def backtracking(nums, startIndex):
            res.append(path[:])
        #确定终止条件
            if startIndex >= len(nums):
                return
        #单层递归条件
            for i in range(startIndex,len(nums)):
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()
        backtracking(nums, 0)
        return res  
            
https://blog.csdn.net/qwe954443563/article/details/110388570