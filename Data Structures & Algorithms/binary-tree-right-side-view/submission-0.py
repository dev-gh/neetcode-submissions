'''
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,4,null,5]

Output: [1,3,5]

Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Example 3:

Input: root = [1,null,2]

Output: [1,2]

Example 4:

Input: root = []

Output: []


Constraints:

    0 <= number of nodes in the tree <= 100
    -100 <= Node.val <= 100



Topics


Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the given tree.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        current = deque()
        current.append(root)
        children = deque()

        while current:
            node = current.popleft()

            if node.left is not None:
                children.append(node.left)

            if node.right is not None:
                children.append(node.right)

            if not current:
                result.append(node.val)
                current = children
                children = deque()

        return result

        