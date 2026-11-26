# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_kth_node(self, temp: ListNode | None, k: int) -> ListNode | None:
        k -= 1
        while temp is not None and k > 0:
            k -= 1
            temp = temp.next
        return temp

    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        temp = head
        prev_last = None

        while temp is not None:
            kth_node = self.get_kth_node(temp, k)
            if kth_node is None:
                if prev_last is not None:
                    prev_last.next = temp
                break

            next_node = kth_node.next
            kth_node.next = None  # Temporarily isolate the k-group

            reversed_head = self.reverse_list(temp)

            if temp == head:
                head = reversed_head
            else:
                prev_last.next = reversed_head

            prev_last = temp
            temp = next_node

        return head