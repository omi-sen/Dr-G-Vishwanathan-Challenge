from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Split the list into two halves
        mid = self.getMid(head)
        right = mid.next
        mid.next = None  # Break the link to separate the two halves
        
        # Recursively sort both halves
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right)
        
        # Merge the two sorted halves
        return self.merge(left_sorted, right_sorted)
    
    def getMid(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Attach any remaining nodes
        tail.next = list1 if list1 else list2
            
        return dummy.next
