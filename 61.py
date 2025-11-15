# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return None
        if head and head.next==None:
            return head
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        k=k%length
        if k==0:
            return head
        for i in range(k):
            temp=head
            prev=None
            while temp.next:
                prev=temp
                temp=temp.next

            temp.next=head
            head=temp
            prev.next=None

        return head


        
