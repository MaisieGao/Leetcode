
import random
https://leetcode.cn/problems/random-pick-with-weight/solution/tu-jie-an-quan-zhong-sui-ji-xuan-ze-zhi-pu1mv/
def __init__(self, w: List[int]):
    n = len(w)
    self.sum = [0]*(n+1)
    
    for i in range(1,n+1):
        self.sum[i] = self.sum[i-1] + w[i-1]

def pickIndex(self) -> int:
    #randomly pick a number from [1,最后一个数]
    d = random.randint(1,self.sum[-1])
    l = 1;r = len(self.sum)-1
    while l <= r:
        #It returns the average of l and r, rounded down
        mid = (l+r)>>1
        if self.sum[mid] >= d:
            r = mid - 1
        else:
            l = mid + 1
    index = l - 1
    return index

        