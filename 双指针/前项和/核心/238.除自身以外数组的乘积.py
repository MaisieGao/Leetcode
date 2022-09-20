https://leetcode.cn/problems/product-of-array-except-self/solution/gan-jue-da-bu-fen-ti-jie-du-shi-tie-dai-ma-jia-fu-/
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    #总共有n个(没有n+1个，因为不包括自身)
    l = [1] * n
    r = [1] * n
    res = [1] * n
        for i in range(1, n):
            l[i] = nums[i-1] * l[i-1]
        for j in range(n-2, -1, -1):
            r[j] = nums[j+1] * r[j+1]
        for k in range(n):
            res[k] = l[k] * r[k]
    return res