#运用双指针，i 和 j
#i 是起点，j先爬前半段，再爬后半段，然后记录j到i的长度(j - i + 1)
#再去找下一个山，所以山要用while
#注意i和j的boundary

def longestMountain(self, A: List[int]) -> int:
        res = 0
        i, j = 0, 0  # i 指针用于标注山脉起始坐标，j 指针用于标注山脉结束坐标
        while i < len(A) - 2:  # 保证序列至少含有 3 个元素
            # 1. 移动 i 指针，寻找起始坐标
            while i < len(A) - 1 and A[i] >= A[i + 1]:
                i += 1
            # 2. 找到起始坐标后，开始移动 j 指针寻找连续上升序列
            j = i
            #要让j能往后移，就必须j的后面一个也是valid的，所以j不能<=len(A)-1
            while j < len(A) - 1 and A[j + 1] > A[j]:
                j += 1
            # 3. 记录当前峰顶元素，用于后续连续序列的判断
            summit = A[j]
            # 4. 找到峰顶坐标后，继续移动 j 指针寻找连续下降序列
            while j < len(A) - 1 and A[j] > A[j + 1]:
                j += 1 
            # 5. 记录当前连续序列的长度，寻找最大值
            if A[i] < summit and summit > A[j]:
                res = max(res, j - i + 1)
            # 6. 寻找下一个连续序列的起始坐标
            i = j
        return res