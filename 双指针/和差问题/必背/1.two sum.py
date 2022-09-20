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
        if diff in preMap.keys():
            # value->left index
            return [preMap[diff], index]
        else:
            #diff是以前已经放进去的n
            #如果premap里没有diff的时候，要放进去n
            preMap[element] = index
        
#第二种解法
def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            
            diff = target - nums[i]
            if diff in hashmap.keys():
                return [hashmap.get(diff,0),i]
            else:
                hashmap[nums[i]] = i