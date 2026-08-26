'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

Input: root = [1,2,3,4,5], subRoot = [2,4,5]

Output: true


Example 2:

Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

Output: false


Constraints:

    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -10^4 <= root.val <= 10^4
    -10^4 <= subRoot.val <= 10^4



Topics


Recommended Time & Space Complexity

You should aim for a solution as good or better than O(m * n) time and O(m + n) space, where n and m are the number of nodes in root and subRoot, respectively.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        matches = [] 
        nonvisited = [root]

        while len(nonvisited) != 0:
            node = nonvisited.pop()
            if node.val == subRoot.val:
                matches.append(node)
            
            if node.left is not None:
                nonvisited.append(node.left)

            if node.right is not None:
                nonvisited.append(node.right)
                
        for match in matches:
            root_nodes = [match]
            subroot_nodes = [subRoot]
            found = True

            while len(root_nodes) != 0 and len(subroot_nodes) != 0:
                root_node = root_nodes.pop()
                subroot_node = subroot_nodes.pop()

                if root_node is None and subroot_node is None:
                    continue

                if root_node.val != subroot_node.val:
                    found = False
                    break

                if root_node.left is not None and subroot_node.left is not None:
                    root_nodes.append(root_node.left)
                    subroot_nodes.append(subroot_node.left)
                elif root_node.left is None and subroot_node.left is None:
                    pass
                else:
                    found = False
                    break

                if root_node.right is not None and subroot_node.right is not None:
                    root_nodes.append(root_node.right)
                    subroot_nodes.append(subroot_node.right)
                elif root_node.right is None and subroot_node.right is None:
                    pass
                else:
                    found = False
                    break

            if found:
                return True
        
        return False
            



        



