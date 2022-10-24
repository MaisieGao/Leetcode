# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        #快慢指针找中点
        fast,slow = head.next,head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow就是第二个链开始的地方
        #断开第一个和第二个链,拿第二个链的头
        mid = slow.next
        #第一个链的最后是none
        slow.next = None
        #找到中点反转链表
        pre = None
        #第二个链的头是slow.next
        cur = mid
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        reverseHead = pre
        #插入
        left = head
        right = reverseHead
        #right比较短
        while right:
            #在断开连接之前先移到下一个
            leftNext = left.next
            rightNext = right.next
            #让left接right，再接left的下一个
            left.next = right
            right.next = leftNext
            #把left和right都往下移一个，继续接下去
            left = leftNext
            right = rightNext
