# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global count
        count = 0
        def traverse(root, current_max):
            global count
            if root is None:
                return
            if root.val >= current_max:
                count += 1    
            current_max = max(current_max, root.val)
            traverse(root.left, current_max)
            traverse(root.right,current_max)
            return 
        traverse(root, float("-inf"))
        return count