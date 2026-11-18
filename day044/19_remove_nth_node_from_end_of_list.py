from typing import Optional

# Definition for singly-linked list (already provided by LeetCode).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def removeNthFromEnd(
      self, head: Optional[ListNode], n: int
  ) -> Optional[ListNode]:
    # Create a dummy node pointing to head to handle edge cases (like removing the head itself)
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Move fast pointer n + 1 steps ahead so there is a gap of n nodes between slow and fast
    for _ in range(n + 1):
      fast = fast.next

    # Move both pointers until fast reaches the end of the list
    while fast:
      fast = fast.next
      slow = slow.next

    # Skip the nth node from the end
    slow.next = slow.next.next

    return dummy.next
