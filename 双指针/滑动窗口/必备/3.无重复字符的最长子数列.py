https://leetcode.cn/problems/longest-substring-without-repeating-characters/solution/yi-ge-mo-ban-miao-sha-10dao-zhong-deng-n-sb0x/
def lengthOfLongestSubstring(self, s: str) -> int:
    #step1
    #求最长，所以有maxLength
    maxLength = 0
    #无重复，所以用hashmap
    hashmap = {}

    #step2
    start = 0
    for end in range(len(s)):
        #step3 更新需要维护的变量
        # i.e. 把窗口末端元素加入哈希表，使其频率加1
        hashmap[s[end]] = hashmap.get(s[end],0) + 1
        #更新最大长度
        #如果两个相等，说明没有重复元素，这时跟新最大长度
        #这个不能转移到缩小窗口那里，因为缩小窗口的条件是不合法的，
            #而这里我们要找合法的（也就是相等的情况）
        if len(hashmap) == end - start + 1:
            maxLength = max(maxLength, end-start+1)
        
        #step4
        # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
        # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
        # 当窗口长度大于哈希表长度时候 (说明存在重复元素)，窗口不合法
        # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap)
        while end - start + 1 > len(hashmap):
            #调整hashmap
            head = s[start]
            hashmap[head] -= 1
            if hashmap[head] == 0:
                del hashmap[head]
            #缩小窗口
            start += 1
    return maxLength