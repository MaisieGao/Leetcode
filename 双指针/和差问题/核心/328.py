n = len(s)
if n < 3:
    return 0
count = 0
s.sort()
#必须要sort
#[3,4,5,6]
#pos是最大，刚开始a是最小
for pos in range(2, n):
    left = 0
    right = pos - 1
    while left < right:
        if s[left] + s[right] > s[pos]:
        #[3,5,6][4,5,6]
        #right往前移一位[3,4,6]
            count += right - left
            right -= 1
        else:
            left += 1
return count
