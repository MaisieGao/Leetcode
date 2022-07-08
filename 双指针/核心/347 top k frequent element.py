#这道题要跟largest kth 区分开
#largest 要用quickselect
#frequent首先我们要用dict排好序，其实这个题也可以用小跟堆(min-heap)
#O(n) time for buildHeap and pop node k time with each pop take O(logn) time, so the complexity is O(k log n).
#用桶排序的话是o(n)
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #桶排序
    #看到frequent,我们用dict
    n = len(nums)
    count = {}
    # freq是桶，是List of list
    #build 桶和dict我们需要O(n) space

    #不能用 freq = [[] * (n+1)]这样只有[[]]
    freq = [[] for _ in range(len(nums)+1)]
    print(freq)
    res = []
    for i in nums:
        count[i] = 1 + count.get(i, 0)
    for key, value in count.items():
        freq[value].append(key)
    #only go through the elements once, so O(n)
    for i in range(n, 0, -1):
        for j in freq[i]:
            res.append(j)
            if len(res) == k:
                return res