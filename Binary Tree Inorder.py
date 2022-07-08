# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(node):
            nonlocal node_values
            
            if node is None:
                return
            
            traverse(node.left)
            
            node_values.append(node.val)
            
            traverse(node.right)
            
        node_values = []
        traverse(root)
        return node_values
        