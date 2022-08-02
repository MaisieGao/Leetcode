def maximumUniqueSubarray(self, nums: List[int]) -> int:
    sum = 0
    maxSum = 0
    hashmap = {}
    start = 0
    for end in range(len(nums)):
        sum += nums[end]
        hashmap[nums[end]] = hashmap.get(nums[end],0) + 1
        if end - start + 1 == len(hashmap):
            maxSum = max(sum, maxSum)
        
        while end - start + 1 > len(hashmap):
            head = nums[start]
            hashmap[head] -= 1
            if hashmap[head] == 0:
                del hashmap[head]
            sum -= head
            start += 1
    return maxSum