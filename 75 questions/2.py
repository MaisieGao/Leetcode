# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2
        t = dummy = ListNode(0)
        carry = 0

        #if there is still a carry, don't stop the while loop
        while p or q or carry:
            
            v1 = p.val if p else 0
            v2 = q.val if q else 0

            #get total sum include carry
            sum = v1 + v2 + carry
            val = sum % 10
            #get new carry
            carry = sum // 10
            #create the next node with value as val
            t.next = ListNode(val)
            #switch to the next node
            t = t.next
            #move forward with l1 and l2
            if p:
                p = p.next
            if q:
                q = q.next
        return dummy.next
 
        

