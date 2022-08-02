https://leetcode.cn/problems/range-sum-query-immutable/solution/-by-huan-huan-20-h5g4/
def __init__(self, nums: List[int]):
        n = len(nums)
        self.dp = [0]*(n+1)
        #我们不用管dp[0],因为dp[0] = nums[0]
        #我们需要求dp[1]...dp[n],因为虽然没有nums[n],但是dp[n]是nums[n-1]和dp[n-1]的和
        #最重要的一点是dp[i]是从0加到i-1,所以dp[i-1]是从0到i-2再加上nums[i-1]，正好是dp[i-1]
        for i in range(1,n+1):
            self.dp[i] = self.dp[i-1] * nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right+1] - self.dp[left]