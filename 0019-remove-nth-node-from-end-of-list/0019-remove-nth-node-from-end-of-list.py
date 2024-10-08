# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        right_node = head
        left_node = dummy
        while n != 0:
            right_node = right_node.next
            n -= 1

        while right_node:
            left_node = left_node.next
            right_node = right_node.next
    
        left_node.next = left_node.next.next
        return dummy.next
        