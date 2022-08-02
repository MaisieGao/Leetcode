def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    a = 0
    b = 0
    temp =[]
    while a < len(nums1) and b < len(nums2):
        if nums1[a] > nums2[b]:
            temp.append(nums2[b])
            b += 1
        else:
            temp.append(nums1[a])
            a +=1
    while a < len(nums1):
        temp.append(nums1[a])
        a += 1
    while b < len(nums2):
        temp.append(nums2[b])
        b += 1
    print(temp)
    if len(temp) %2 == 0:
        mid = len(temp) // 2
        print(mid)
        median = (temp[mid]+temp[mid-1])/2
    else:
        mid = len(temp) // 2
        
        median = temp[mid]
    return median