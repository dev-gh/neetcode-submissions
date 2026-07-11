'''
Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]

Example 2:

Input: head = [5], n = 1

Output: []

Example 3:

Input: head = [1,2], n = 2

Output: [2]

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        first = head
        while first is not None:
            first = first.next
            length += 1

        if length - n == 0:
            return head.next

        prev_to_n_th_index = length - n - 1
        print(f'{prev_to_n_th_index=}')

        second = head
        while prev_to_n_th_index != 0:
            prev_to_n_th_index -= 1
            second = second.next

        print(f'{second.val=}')
        second.next = second.next.next

        return head
