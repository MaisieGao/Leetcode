https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/solution/fu-xue-ming-zhu-dong-hua-ti-jie-bang-zhu-yrx5/
#要搞清楚两个指针分别指向什么，慢指针指向即将判断的字符，然后快指针指向替换的字符，然后 nums[fast]==nums[slow-2] 这个公式非常巧妙，如果相等的话，说明 slow 指向的字符至少出现了三次，
def removeDuplicates(self, nums: List[int]) -> int:
    def solve(k):
        slow = 0
        #fast 是从头到尾过一遍
        for fast in range(len(nums)):
            #符合（重复）的时候才赋值和移动slow
            #不符合的时候不动，只移动fast
            if slow < k or nums[fast] != nums[slow-k]:
                nums[slow] = nums[fast]
                slow+=1
        #[1,1,1,2,2,3]
        #slow 现在位置的point to 最后一个3, 也就是说slow 
        # point to the next element of all the element it needed
        #所以size 正好等于slow
        #return slow就是return 现在的size
        return slow
    return solve(2)