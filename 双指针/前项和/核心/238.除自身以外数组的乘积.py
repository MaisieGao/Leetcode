https://leetcode.cn/problems/product-of-array-except-self/solution/gan-jue-da-bu-fen-ti-jie-du-shi-tie-dai-ma-jia-fu-/
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    #总共有n个
    l = [1] * n
    r = [1] * n
    res = []
    for i in range(1,n):
        l[i] = l[i-1] * nums[i-1]
    #是从（0,n-1），但是是反的
    for i in range(n-2, -1,-1):
        r[i] = r[i+1] * nums[i+1]
    for i in range(n):
        res.append(l[i]*r[i])
    return res