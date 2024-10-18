# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if head is None:
            return True
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        
    def dfs(self, head, root):
        if head is None:
            return True
        if not root or root.val != head.val:
            return False
        if head.val == root.val:
            return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)