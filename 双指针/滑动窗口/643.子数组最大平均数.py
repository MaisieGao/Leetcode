def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Step 1
        # 定义需要维护的变量
        # 本题求最大平均值 (其实就是求最大和)，所以需要定义sum_, 同时定义一个max_avg (初始值为负无穷)
        sum_, max_avg = 0, -math.inf

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(nums)):
            # Step 3: 更新需要维护的变量 (sum_, max_avg), 不断把当前值积累到sum_上
            sum_ += nums[end]
            if end - start + 1 == k:
                max_avg = max(max_avg, sum_ / k)

            # Step 4
            # 根据题意可知窗口长度固定，所以用if
            # 窗口首指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (sum_)
            if end >= k - 1: #到达了固定长度
                sum_ -= nums[start]
                start += 1
        # Step 5: 返回答案
        return max_avg


