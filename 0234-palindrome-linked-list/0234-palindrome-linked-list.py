# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=head
        fast=head
        prev=None

        while fast and fast.next:
            fast=fast.next.next

            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt

        if fast:
            slow=slow.next

        while prev and slow:
            if prev.val!=slow.val:
                return False

            prev=prev.next
            slow=slow.next

        return True