class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []
        def backtracking(openN,closeN):
            #end
            if openN == closeN == n:
                res.append("".join(stack))
                return
            #if not end
            #when can add openN
            if openN < n:
                #add first
                stack.append('(')
                #backtrack
                backtracking(openN + 1, closeN)
                #pop back
                stack.pop()
            #when can add closeN
            if openN > closeN:
                stack.append(')')
                backtracking(openN, closeN + 1)
                stack.pop()
        backtracking(0,0)
        return res
