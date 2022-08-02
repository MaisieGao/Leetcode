https://leetcode.cn/problems/random-pick-with-weight/solution/yi-bu-yi-bu-you-hua-dao-qian-zhui-he-er-177nl/
def __init__(self, w):
    """
    :type w: List[int]
    """
    n = len(w)
    self.dp = [0] * n
    self.dp[0] = w[0]
    for i in range(1, n):
        self.dp[i] = self.dp[i-1] + w[i]

def pickIndex(self):
    """
    :rtype: int
    """
    t = random.randint(1,self.dp[-1])
    index = bisect_left(self.dp, t)
    return index
        