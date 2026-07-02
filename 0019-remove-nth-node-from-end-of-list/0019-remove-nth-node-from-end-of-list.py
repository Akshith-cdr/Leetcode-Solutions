# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp=ListNode(0,head)

        slow,fast=temp,temp

        for _ in range(n+1):
            fast=fast.next
        
        while fast is not None:
            slow=slow.next
            fast=fast.next
        
        slow.next=slow.next.next
        return temp.next