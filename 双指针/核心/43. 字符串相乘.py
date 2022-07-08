def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        ans = [0] * (m+n)
        for i in range(m-1, -1, -1):
            a = int(num1[i])
            for j in range(n-1, -1, -1):
                b = int(num2[j])
                #2位数*2位数=四位数
                #i最大是1，j最大是1，最大是3，那就是4个数
                #最右边的位置是a+b
                ans[i+j+1] += a * b
        #从最右到最左，最小到最大
        for i in range(m+n-1, 0, -1):
            #上一位要加下一位//10的进位
            ans[i-1] += ans[i] // 10
            #剩下的那一位是剩余的数
            ans[i] %= 10
        #为了让第一位不是0
        beg = 1 if ans[0] == 0 else 0
        #把ans里从beg开始的每个数字都变成字母
        ans = map(str, ans[beg:])
        #把字母合起来
        return ''.join(ans)