def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Step 1: 定义需要维护的变量, 本题求最小长度，所以需要定义min_len, 本题又涉及求和，因此还需要一个sum变量
        #len(nums)+1 is something you could never reach if sum never add up to target
        min_len, sum_ = len(nums)+1, 0

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(nums)):
            # Step 3: 更新需要维护的变量 (min_len, sum_)
            sum_ += nums[end]

            # Step 4
            # 这一题这里稍微有一点特别: sum_ >= target其实是合法的，但由于我们要求的是最小长度，
            # 所以当sum_已经大于target的时候继续移动右指针没有意义，因此还是需要移动左指针慢慢逼近答案
            # 由于左指针的移动可能影响min_len和sum_的值，因此需要在移动前将它们更新
            while sum_ >= target:
                min_len = min(min_len, end - start + 1)
                sum_ -= nums[start]
                start += 1
        # Step 5：返回答案 (最小长度)
        if min_len == len(nums)+1:
            return 0
        return min_len

