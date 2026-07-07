'''
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]

Example 2:

Input: head = []

Output: []

Constraints:

    0 <= The length of the list <= 1000.
    -1000 <= Node.val <= 1000

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node is not None:
            orig_next = node.next
            node.next = prev
            prev = node

            node = orig_next
            # if orig_next != None:
                # node = orig_next
            # else:
                # break

        return prev

        