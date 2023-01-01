class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = [] #every component includes [element, index]

        for i, ele in enumerate(temperatures):
            #when the next element is larger than the front element in the stack
            #the reason using while is because the next element can be larger than several element on the front of stack
            #stack[-1] is the last element in the list (which is the front element in the stack)
            while stack and ele > stack[-1][0]:
                #pop the front element
                stackele, stackindex =stack.pop()
                #mark the difference in the res
                res[stackindex] = i - stackindex 
            #after pop all the element that is smaller, append the element in the stack
            stack.append((ele,i))
            #since already marked 0, if there is no element that is larger than the corresponding one, it is marked 0 already
        return res
