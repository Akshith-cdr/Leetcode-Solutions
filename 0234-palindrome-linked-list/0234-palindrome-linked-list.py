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
        stack=[]
        temp=head

        while temp:
            stack.append(temp.val)
            temp=temp.next
        
        temp=head

        while temp:
            if temp.val!=stack[-1]:
                return False
            
            stack.pop()
            temp=temp.next
        
        return True