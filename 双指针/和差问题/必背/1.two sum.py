def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    preMap = {} 
    #key: value
    #val: index
    for index, element in enumerate(nums):
        diff = target - element
        #查diff在不在hashmap里，如果在，得到index是right，diff的index是left
        #如果不在，把val:index放进hashmap里
        if diff in preMap:
            # value->left index
            return [preMap[diff], index]
        else:
            preMap[element] = index
        

