from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        maxH = max(leftHeight,rightHeight)
        minH = min(leftHeight,rightHeight)
        if (maxH - minH) > 1:
            return False
        elif self.isBalanced(root.left) and self.isBalanced(root.right): 
            return True
    def height(self,node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        leftSide = self.height(node.left)
        rightSide = self.height(node.right)

        return max(leftSide,rightSide) + 1
