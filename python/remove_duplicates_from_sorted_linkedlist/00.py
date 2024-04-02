# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        
        left = right = head
        
        while right.next:
            left = right
            while (right.next) and right.val == right.next.val:
                right = right.next
                
            left.next = right.next
            if right.next:
                right = right.next
            
        return head
