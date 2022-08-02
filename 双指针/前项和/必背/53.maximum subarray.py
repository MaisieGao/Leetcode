https://leetcode.cn/problems/maximum-subarray/solution/53-zui-da-zi-xu-he-by-edelweisskoko-3g6r/
def maxSubArray(self, nums: List[int]) -> int:
    if not nums:
            return 0
    res = float('-inf')
    subMax = float('-inf')
    for i in range(len(nums)):
        if subMax >= 0:
            subMax = subMax + nums[i]
        else:
            subMax = nums[i]
        res = max(res, subMax)
    return res