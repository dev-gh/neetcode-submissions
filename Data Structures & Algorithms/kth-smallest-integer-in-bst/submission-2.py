# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        container = []
        inorder = []

        while current or container:
            if current is not None:
                #print(f'{current.val=}')
                container.append(current)
                current = current.left
            else:
                visited = container.pop()
                inorder.append(visited.val)
                #print(f'{inorder=}')

                current = visited.right
            
        return inorder[k - 1]
        
                
