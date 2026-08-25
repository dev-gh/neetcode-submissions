'''
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:

Input: p = [1,2,3], q = [1,2,3]

Output: true

Example 2:

Input: p = [4,7], q = [4,null,7]

Output: false

Example 3:

Input: p = [1,2,3], q = [1,3,2]

Output: false

Constraints:

    0 <= The number of nodes in both trees <= 100.
    -100 <= Node.val <= 100

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False
          
        nodes_p = [p] 
        nodes_q = [q]

        while len(nodes_p) != 0:
            node_p = nodes_p.pop()
            node_q = nodes_q.pop()

            if node_p is not None and node_q is not None:
                if node_p.val != node_q.val:
                    return False
                
                nodes_p.append(node_p.left)
                nodes_p.append(node_p.right)
                nodes_q.append(node_q.left)
                nodes_q.append(node_q.right)
                continue
            
            if node_p is None and node_q is None:
                continue

            return False
        
        return True
                
            

       