# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.array = []
        self.current = head
        while self.current:
            self.array.append(self.current.val)
            self.current = self.current.next

    def getRandom(self) -> int:
        
        return self.array[random.randrange(len(self.array))] 


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()