https://leetcode.cn/problems/combination-sum/solution/by-huan-huan-20-k3hb/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        def backtrack(candidates,target, sum, startIndex):
            #end
            if sum > target:
                return
            elif sum == target:
                res.append(path[:])
                return
            #单个
            for i in range(startIndex,len(candidates)):
                path.append(candidates[i])
                sum += candidates[i]
                backtrack(candidates,target,sum,i)
                path.pop()
                sum -= candidates[i]
        backtrack(candidates, target, 0, 0)
        return res
