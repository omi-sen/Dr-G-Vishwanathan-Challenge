from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases: empty list, single node, or no rotation
        if not head or not head.next or k == 0:
            return head
        
        # 1. Find the length of the list and the current tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # 2. Calculate effective rotations needed
        k = k % length
        if k == 0:
            return head
        
        # 3. Connect tail to head to form a ring
        tail.next = head
        
        # 4. Find the new tail: (length - k) steps from the current tail
        steps_to_new_tail = length - k
        new_tail = tail
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        # 5. Set the new head and break the ring
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
