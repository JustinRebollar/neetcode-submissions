# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
curr 0,1,2,3
-    ^
     0
-      ^
     cur + prev
     1,0
-        ^
     cur + prev
     2,1,0
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = None

        curr_node = head
        while curr_node:
            next_node = curr_node.next

            curr_node.next = reversed_list
            reversed_list = curr_node

            curr_node = next_node

        return reversed_list