# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        results = []
        def dfs(root, s):
            if not root:
                return
            if root.left or root.right:
                s += str(root.val) + '->'
            else:
                s += str(root.val)
            if not root.left and not root.right:
                results.append(s)
            dfs(root.left, s)
            dfs(root.right, s)

        dfs(root, "")
        return results
        