class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        length =0 
        maxLength = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                length = right - left + 1
                maxLength = max(maxLength, length)
            else:
                left = right + 1
        return maxLength