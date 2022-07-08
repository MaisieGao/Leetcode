https://leetcode.cn/problems/odd-even-linked-list/solution/qi-ou-lian-biao-by-leetcode-solution/

#只维护了指针，所以space O(1)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #先连接所有的奇数节点
        #再让所有的偶数节点在一起
        #再用最后一个奇数节点连接偶数节点的第一个
        if not head:
            return None
        odd = head
        firstEven=even = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next 
            even = even.next 
        odd.next = firstEven
        return head