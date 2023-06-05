class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates = sorted(candidates)
        def dfs(path,remain,startindex):
            if remain ==0:
                res.append(path[:])
                return
           
            for i in range(startindex,len(candidates)):
                #if 
                if candidates[i] > remain:
                    return
                if i > startindex and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(path,remain-candidates[i],i+1)
                path.pop()
        dfs([],target,0)
        return res
        