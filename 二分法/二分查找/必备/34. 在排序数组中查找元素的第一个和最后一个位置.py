def searchRange(self, nums: List[int], target: int) -> List[int]:
        #首先找左边的
        def searchLeft(nums, target):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            #在什么时候return -1, left是往大了走
            #right都取不到len(nums), left肯定取不到len(nums)
            if left >= len(nums) or nums[left] != target:
                return -1
            else:
                return left
        def searchRight(nums,target):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if right < 0 or nums[right] != target:
                return -1
            else:
                return right
        left = searchLeft(nums,target)
        right = searchRight(nums,target)
        res = [left,right]
        return res
                    
            