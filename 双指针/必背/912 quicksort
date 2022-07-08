def sortArray(self, nums: List[int]) -> List[int]:
    #先得到pivot的Index
    def partition(nums, left, right):
        #选个位置做partition
        m = randint(left, right)
        #让pivot在最后
        nums[m], nums[right] = nums[right], nums[m]
        pivot = nums[right]

        #j is the left pointer
        j = left
        #i is the right pointer
        for i in range(left, right):
            #if nums[i] > pivot, let it stay, i continue go right, j stay. so when 
            #left pointer only moves when qualified.
            #only swap when qualified
            if nums[i] <= pivot:
                nums[j],nums[i] = nums[i], nums[j]
                j+=1
        #after all the swap, smaller than pivot is on the front, larger than the pivot is after, the last element is the pivot
        #left point to the first larger than pivot index
        nums[j], nums[right] = nums[right], nums[j]
        #全部换完
        return j
    #quicksort是找到了index的位置，然后他前面的和后面的分别进行quicksort,除了index以外
    def quickSort(nums, left, right):
        if left >= right:
            return
        index = partition(nums, left,right)
        quickSort(nums, left, index-1)
        quickSort(nums, index+1, right)
    quickSort(nums,0, len(nums)-1)
    return nums