# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current = node
        while current.next:
            if current.next.next == None:
                current.val = current.next.val
                current.next = None
            else:
                current.val = current.next.val
                current = current.next
        
        