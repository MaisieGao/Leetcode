def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        maxLength = 0
        start = 0
        for end in range(len(nums)):
            product *= nums[end]
            
            while product >=k and end >= start:
                product /= nums[start]
                start += 1
            # //每次右指针位移到一个新位置，应该加上 x 种数组组合：
            # //  nums[right]
            # //  nums[right-1], nums[right]
            # //  nums[right-2], nums[right-1], nums[right]
            # //  nums[left], ......, nums[right-2], nums[right-1], nums[right]
            # //共有 right - left + 1 种

         maxLength += end - start + 1
        return maxLength