from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        if node is None:
            return None
        self.swapNodes(node)
        self.invertTree(node.left)
        self.invertTree(node.right)
        return root
    def swapNodes(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = node.right
        node.right = node.left
        node.left = temp
        return node
    def invertTreeDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                temp = node.right
                node.right = node.left
                node.left = temp
                stack.extend([node.right,node.left])
        return root
