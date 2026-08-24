'''
Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:

Input: root = [1,2,3,null,null,4]

Output: true

Example 2:

Input: root = [1,2,3,null,null,4,null,5]

Output: false

Example 3:

Input: root = []

Output: true

Constraints:

    The number of nodes in the tree is in the range [0, 1000].
    -1000 <= Node.val <= 1000

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), TypeGuard:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        nonvisited = [root]
        visited = []

        while len(nonvisited) != 0:
            node = nonvisited.pop()
            visited.append(node)

            if node.left is not None:
                nonvisited.append(node.left)

            if node.right is not None:
                nonvisited.append(node.right)

    
        heights = {}
        while len(visited) != 0:
            subn = visited.pop()
            left = heights.get(subn.left, 0)

            if subn.left is not None:
                left += 1

            right = heights.get(subn.right, 0)
            if subn.right is not None:
                right += 1

            if abs(right - left) > 1:
                return False

            heights[subn] = max(left, right)
       
        return True





    