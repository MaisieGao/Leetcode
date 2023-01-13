class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        alt = set()
        m = len(heights)
        n = len(heights[0])
        # to check whether (r,c) is visited
        # and whether the current height is larger than previous height
        def dfs(r,c,visit,previousHeight):
            #if not qualified, not included
            if ((r,c) in visit or r <0 or c < 0 or r >= m or c >= n or heights[r][c] < previousHeight):
                return
            #if quailified, add it in visited set
            visit.add((r,c))
            # in four directions, compare the current height with the previous height(the current height now become the previous height in next round)
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        # for each row,
        for r in range(m):
            #start from nodes the first column
            dfs(r,0,pac,heights[r][0])
            #start from nodes the last column 
            dfs(r,n-1,alt,heights[r][n-1])
        for c in range(n):
            #start from nodes the first row
            dfs(0,c,pac,heights[0][c])
            #start from nodes the last row
            dfs(m-1,c,alt,heights[m-1][c])
        
        #check whether the node is in both pac and alt, if it is, attach it in res
        res = []
        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in alt:
                    res.append((i,j))
        return res