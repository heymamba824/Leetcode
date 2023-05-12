class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head 
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet = fast
                start = head 
                while meet != start:
                    meet = meet.next
                    start  = start.next
                return meet    
            
        return None
