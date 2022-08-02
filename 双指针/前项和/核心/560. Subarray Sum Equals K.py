def subarraySum(self, nums: List[int], k: int) -> int:
    #先有sum, res,还有一个hashmap
    #hashmap里面存储的是【prefix_sum, count】prefix_sum也是diff
    sum = 0
    res = 0
    #刚开始有一个sum是0的时候，就是里面没有任何元素的时候，这个box的数量是1
    prefix_sum = {0:1}  
    #开始加prefix
    for num in nums:
        sum += num
        #找出sum和k的差，去hashmap里面找diff = prefix_sum,如果存在，说明有box的和是k(sum-前面的prefix_sum)
        diff = sum - k
        res += prefix_sum.get(diff, 0)
        #sum进hashmap,作为diff, value + 1
        prefix_sum[sum] = 1 + prefix_sum.get(sum,0)
    return res