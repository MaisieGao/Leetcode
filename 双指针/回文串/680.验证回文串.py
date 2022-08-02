def validPalindrome(self, s: str) -> bool:
    left = 0
    right = len(s)-1
    while left < right:
        #最边上的两个不相等时，我们看删除一个是否剩余的是回文串
        if s[left] != s[right]:
            #删除左边的得到重新的string
            #right+1是因为我们要取到right必须right+1
            arrRight = s[left+1:right+1]
            #删除右边的得到重新的string
            #right是因为我们不取right
            arrLeft = s[left: right]
            #看arrRight和arrLeft正的和反过来的是否一致,一致就是true
            return (arrRight == arrRight[::-1] or arrLeft == arrLeft[::-1])
        else:
            #最边上的相等时我们移进来两个，看新的两个是否相等
            left += 1
            right -= 1
    return True