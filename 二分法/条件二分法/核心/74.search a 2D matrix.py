def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #首先是row和column
        row = len(matrix)
        column = len(matrix[0])
        #每一个row我们filter.用log m筛出我们需要的row
        top = 0 
        bottom = row - 1
        while top <= bottom:
            midRow = (top + bottom) // 2
            #比最小的小，就要上一行(bottom往上移)
            if target < matrix[midRow][0]:
                bottom = midRow - 1
            #比最大的大，就要下一行（top往下移）
            elif target > matrix[midRow][-1]:
                top = midRow + 1
            #在对的行，break,进入一行里element的查找
            else:
                break
        #如果到最后都没找到target,top > bottom
        if top>bottom:
            return False
        #找那行里的值
        left = 0
        right = column - 1
        #我们在上一个while loop里面找到的row
        row = (top+bottom)//2
        while left <= right:
            mid = (left+right)//2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False