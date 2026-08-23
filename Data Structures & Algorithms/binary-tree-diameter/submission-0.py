'''
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

Given the root of a binary tree root, return the diameter of the tree.

Example 1:

Input: root = [1,null,2,3,4,5]

Output: 3

Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:

Input: root = [1,2,3]

Output: 2

Constraints:

    1 <= number of nodes in the tree <= 100
    -100 <= Node.val <= 100

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'NON OPTIMAL'
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        unchecked_nodes = [root] 
        all_nodes = []

        # Collecting all nodes
        while len(unchecked_nodes) != 0:
            node = unchecked_nodes.pop()
            # print(f'{node.val=}')
            all_nodes.append(node)

            left, right = node.left, node.right

            if left is not None:
                unchecked_nodes.append(left)
            
            if right is not None:
                unchecked_nodes.append(right)

        # Now checking all nodes depths for left and right nodes
        diameter = 0
        for node in all_nodes:
            left_height = 0
            sub_nodes = []

            if node.left is not None:
                sub_nodes.append((node.left, 1))
           
            while len(sub_nodes) != 0:
                current, height = sub_nodes.pop()
                left, right = current.left, current.right
                left_height = max(left_height, height)
    
                if left is not None:
                    sub_nodes.append((left, height + 1))
                
                if right is not None:
                    sub_nodes.append((right, height + 1))

            right_height = 0
            if node.right is not None:
                sub_nodes.append((node.right, 1))
            
            while len(sub_nodes) != 0:
                current, height = sub_nodes.pop()
                left, right = current.left, current.right
                right_height = max(right_height, height)
    
                if left is not None:
                    sub_nodes.append((left, height + 1))
                
                if right is not None:
                    sub_nodes.append((right, height + 1))
            
            diameter = max(diameter, left_height + right_height)
            # print(f'{node.val=}, {left_height=}, {right_height=}, {diameter=}')

        return diameter

    