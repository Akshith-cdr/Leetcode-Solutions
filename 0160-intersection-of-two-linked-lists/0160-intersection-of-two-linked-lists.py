# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        d1,d2=headA,headB

        while d1!=d2:
            if d1 is None:
                d1=headB
            else:
                d1=d1.next
            
            if d2 is None:
                d2=headA
            else:
                d2=d2.next
        
        return d1