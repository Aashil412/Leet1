# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1) If the LL is empty, []
        2) have a pointer that will connect the tail to the head
        3) have a previous variable that will be right b4 the new head
        """
        if head is None:
            return head
        tail = head
        count = 1
        while tail.next != None:
            tail = tail.next
            count += 1
        tail.next = head

        current = head
        k = k % count
        for i in range(count - k - 1):
            current = current.next
        newHead = current.next
        current.next = None
        return newHead
