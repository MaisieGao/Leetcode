def search(self, nums: List[int], target: int) -> int:
        #首先要define left, right and mid
        left = 0
        right = len(nums) - 1
        #只要有boundary左移或者右移，就要用while loop
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            #判断mid在左边还是右边,在左边
            if nums[mid] >= nums[left]:
                #判断target的位置，target在右边
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            #mid在右边
            else:
                #target在mid左边
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1