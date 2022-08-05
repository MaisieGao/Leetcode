def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    res, temp = [],[]
    def kSum(k, start, target):
        if k != 2:
            for i in range(start, len(nums)-k+1):
                temp.append(nums[i])
                #temp是除了twosum前面的数
                print('temp',temp)
                kSum(k-1,i+1,target-nums[i])
                temp.pop()
                print('temp1',temp)
            return
        #2sum
        l, r = start, len(nums)-1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1  
            else:
                res.append(temp + [nums[l],nums[r]])   
                                
                print('res',res)
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    kSum(4, 0, target)
    return res

    nums = [1,0,-1,0,-2,2]
    target = 0
    ('temp', [-2])
    ('temp', [-2, -1])
    ('res', [[-2, -1, 1, 2]])
    ('temp1', [-2])
    ('temp', [-2, 0])
    ('res', [[-2, -1, 1, 2], [-2, 0, 0, 2]])
    ('temp1', [-2])
    ('temp', [-2, 0])
    ('temp1', [-2])
    ('temp1', [])
    ('temp', [-1])
    ('temp', [-1, 0])
    ('res', [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
    ('temp1', [-1])
    ('temp', [-1, 0])
    ('temp1', [-1])
    ('temp1', [])
    ('temp', [0])
    ('temp', [0, 0])
    ('temp1', [0])
    ('temp1', [])

