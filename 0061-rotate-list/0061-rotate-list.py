# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k==0:
            return head
           
        l=1
        tail=head

        while tail.next:
            tail=tail.next
            l+=1
        
        k=k%l
        if k==0:
            return head

        tail.next=head

        n=l-k
        ntail=head

        for _ in range(n-1):
            ntail=ntail.next
        
        nhead=ntail.next
        ntail.next=None
        return nhead