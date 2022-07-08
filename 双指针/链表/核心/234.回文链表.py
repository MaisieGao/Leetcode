#如果是中间啊或者什么时候链表要取reverse
#可以取reverse(用recursive 或者iterative)
#可以用stack(stack会比较好想)，但是stack的空间复杂度是O(n)
#这道题要求的空间复杂度是O（1）,就是在原链表中进行比较
#回文的特点就是后半段必须倒过来，所以要取middle,middle后面要进行reverse
#链表要看是奇数还是偶数nodes
#递归的空间是o(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        #get middle
        #如果是奇数，要Middle后面的一个Node作为终点node
        #如果是偶数，不用变，middle本来就是终点Node
        def middle(head):
            fast = slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            if fast:
                slow = slow.next 
            return slow
        #用reverse
        def reverse(head):
            pre = None
            cur = head 
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre
        index = middle(head)
        right = reverse(index)
        left = head
        #两个pointer, 一个从reverse的head开始（也就是最右侧），一个从head开始，也就是最左侧。right在不是null的时候，如果是回文链表，就要val全部相等（left如果是奇数多一个node,所以不能是while left）
        while right:
            if right.val != left.val:
                return False
            #两个pointer都要往后挪
            left = left.next
            right = right.next
        return True