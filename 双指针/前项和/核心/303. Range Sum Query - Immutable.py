https://leetcode.cn/problems/range-sum-query-immutable/solution/-by-huan-huan-20-h5g4/
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return None
        n = len(nums)
        self.presum = [0] * (n+1)
        # when i = 0, there is no i-1
        for i in range(1, n+1):
            self.presum[i] = self.presum[i-1] + nums[i-1]
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.presum[right+1]
        else:
            return self.presum[right+1] - self.presum[left]