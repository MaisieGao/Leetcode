def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        #最后一个速度是最大的速度，肯定能吃完，但我们想要最小的速度
        #piles = [3,6,7,11]
        #[1,2,3,...,11] 我们从这些可能的速度来选，所以left = 1, right = 11 which is max(piles)
        #res 是越小越好，所以我们从最大的开始
        res = right
        while left <= right:
            #k是中间的速度
            k = (left+right)//2
            hour = 0
            #我们得到吃完所有需要的时间
            for p in piles:
                hour += math.ceil(p/k)
            #如果能吃完，说明这个k是possible的，我们用res记下这个k,然后让right = k-1去找可能的更小速度
            #第一次k=6,我们把right 变成5，从【1,2。。5】里选
            if hour <= h:
                res = min(res,k)
                right = k - 1
            #不能吃完，说明k这个速度太小了，k和k之前的速度都不能选，所以left 直接是k+1,这道题中，k = 3不可以，我们直接跳到【4,5】
            else:
                left = k+1
        return res
        