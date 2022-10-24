https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solution/by-insist-just-do-it-302a/
# 这道题求的是最小值，我们在判断中数nums[m]时，如果nums[m] > nums[len]，那么中数一定不是最小值，可以放心l=m+1。

# 而如果nums[m] <= nums[len]，我们是不确定中数是否是最小值的，如果直接r=m-1，有可能直接跳过了最小值。

# 例如：nums[]={3,1,2}，第一次nums[m]=1，如果直接r=m-1，第二轮只剩一个3。
https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solution/er-fen-cha-zhao-wei-shi-yao-zuo-you-bu-dui-cheng-z/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:         
                left = mid + 1
            else:                               
                right = mid
        return nums[left]