https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solution/by-insist-just-do-it-302a/
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


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right)//2
            #[3,4,5,1,2]
            if nums[0] <= nums[mid]:
                left = mid + 1
            else: 
                right = mid 
        return nums[left]