# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        next = head
        length = 0
        while next != None:
            length += 1
            next = next.next
        
        mid = length // 2
        cur = head
        while mid:
            mid -= 1
            cur = cur.next
        return cur