# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
https://leetcode.cn/problems/merge-k-sorted-lists/solution/huan-huan-by-huan-huan-20-8bmh/
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        minheap = []
        for list in lists:
            while list:
                heapq.heappush(minheap, list.val)
                list = list.next
        p = dummy = ListNode(0)
        while minheap:
            p.next = ListNode(heapq.heappop(minheap))
            p = p.next
        return dummy.next