'''
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:

Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]

Example 2:

Input: root = [1]

Output: [[1]]

Example 3:

Input: root = []

Output: []

Constraints:

    0 <= The number of nodes in the tree <= 2000.
    -1000 <= Node.val <= 1000

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if None is root:
            return []

        current_level = deque()
        current_level.append(root)
        next_level = deque()
        level_values = []
        values = []
        while len(current_level) != 0:
            node = current_level.popleft()
            level_values.append(node.val)

            if node.left is not None:
                next_level.append(node.left)

            if node.right is not None:
                next_level.append(node.right)

            if len(current_level) == 0:
                values.append(level_values)
                level_values = []

                current_level = next_level
                next_level = deque()
        
        return values
