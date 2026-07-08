'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]

Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]

Example 3:

Input: list1 = [], list2 = []

Output: []

Constraints:

    0 <= The length of the each list <= 100.
    -100 <= Node.val <= 100

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#      k  self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1

        node_1 = list1
        node_2 = list2

        head = None
        current = None

        while node_1 is not None and node_2 is not None:
            if node_1.val <= node_2.val:
                if head is None:
                    head = node_1
                    current = head
                else:
                    current.next = node_1
                    current = node_1

                node_1 = node_1.next
            else:
                if head is None:
                    head = node_2
                    current = head
                else:
                    current.next = node_2
                    current = node_2

                node_2 = node_2.next

        if node_1 is None and current is not None:
            current.next = node_2
        elif node_2 is None and current is not None:
            current.next = node_1
            
        return head










