# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # Find the length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Position of the node to remove from the front
        target_index = length - n

        # Move to the node before the target
        prev = dummy
        for _ in range(target_index):
            prev = prev.next

        # Skip the target node
        prev.next = prev.next.next

        return dummy.next
