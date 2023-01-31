from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d =0
        def height(node):
            if node is None:
                return 0
            nonlocal d
            l = height(node.left)
            r = height(node.right)
            d = max(d,l+r)
            return max(l,r) + 1
        height(root)
        return d