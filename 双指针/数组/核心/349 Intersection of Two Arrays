def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #when value is not limited, it is not efficient to use hashmap,we use set in this case
        #to use hashmap:
        #时间复杂度：O(N)
        #空间复杂度：O(N)
        #we can also use two pointers, but it will be O(n logn)
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)
        for i in nums1:
            count1[i] +=1
        for i in nums2:
            count2[i]+=1
            
        res = []
        for i in count1:
            if i in count2:
                res.append(i)
        return res

        ##方法二：
        #取并集要用&
        #and 用来判断两边的true or false
        return list(set(nums1)&set(nums2))