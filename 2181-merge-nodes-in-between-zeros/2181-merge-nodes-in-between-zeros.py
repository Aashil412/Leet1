# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        zero = 0

        current = head
        total = 0
        current2 = new_head
        while current:
            if current.val == 0:
                zero += 1
            if zero == 2:
                zero -= 1
                current2.val = total
                if current.next is not None:
                    current2.next = ListNode()
                    current2 = current2.next
                total = 0
            total += current.val
            current = current.next                
        return new_head