class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a = 0
        len_b = 0 
        cur = headA
        while cur:
            len_a += 1 
            cur = cur.next
        cur = headB
        while cur:
            len_b += 1
            cur = cur.next
        cur_a = headA
        cur_b = headB
        if len_a > len_b:
            for _ in range(len_a - len_b):
                cur_a = cur_a.next
        else:
            for _ in range(len_b - len_a):
                cur_b = cur_b.next
        while cur_a:
            if cur_a == cur_b:
                return cur_a
            else:
                cur_a = cur_a.next
                cur_b = cur_b.next
        return None
