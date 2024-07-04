# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left,root.right)
    def isMirror(self, rootleft,rootright):
        if rootleft is None and rootright is None:
            return True
        if rootleft is None or rootright is None:
            return False
        return rootleft.val == rootright.val and self.isMirror(rootleft.left, rootright.right) and self.isMirror(rootleft.right,rootright.left)
        