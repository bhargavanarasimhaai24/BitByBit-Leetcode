class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head.next and n==1:
            return None
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        if n==count:
            return head.next
        temp=head
        for i in range(count-n-1):
            temp=temp.next
        popped=temp.next
        temp.next=popped.next
        popped.next=None
        return head
