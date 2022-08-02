# sort: O(nlogn)
# go through the first element use a for loop
#     the second for loop to add up the two sum
# nested loop :O(n^2)
def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    for i, element in enumerate(nums):
        #如果这个数element和上一个相等，直接跳过
        if i >0 and element == nums[i-1]:
            continue
        #2sum的和
        left = i + 1
        right = len(nums)-1
        while left < right:
            sum = element + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            #sum = 0的时候就找到了三个数
            else:
                res.append([element, nums[left],nums[right]])
                #再去找下一个left
                left+=1
                #第二个数left和上一个相等
                while left < right and nums[left] == nums[left-1]:
                    left += 1
    return res