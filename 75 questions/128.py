def longestConsecutive(self, nums: List[int]) -> int:
    numSet=set(nums)
    longest = 0
    for n in numSet:
        #如果这个数字不是连续最小，继续找下一个数字
        #如果是最小，用while加到连续数字没了为止
        if (n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length += 1
            #不一定有一个最小，说不定有几个
            #所以要选出几个length中最长的
            #indentation在这个位置是因为再往前得不到length
            longest = max(length, longest)
    return longest