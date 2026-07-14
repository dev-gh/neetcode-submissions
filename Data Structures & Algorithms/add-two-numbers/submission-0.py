'''
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:

Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.

Example 2:

Input: l1 = [9], l2 = [9]

Output: [8,1]

Constraints:

    1 <= l1.length, l2.length <= 100.
    0 <= Node.val <= 9

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        answer_ptr = answer

        carry = 0
        while l1 is not None or l2 is not None:
            first = 0
            second = 0

            if l1 is not None:
                first = l1.val
                l1 = l1.next if l1.next is not None else None

            if l2 is not None:
                second = l2.val
                l2 = l2.next if l2.next is not None else None

            summ = first + second + carry
            answer_ptr.val = summ if summ < 10 else summ - 10
            carry = 0 if summ < 10 else 1

            if l1 is not None or l2 is not None:
                answer_ptr.next = ListNode()
                answer_ptr = answer_ptr.next
        
        if carry != 0:
            answer_ptr.next = ListNode(carry)

        return answer
        
            
            



            