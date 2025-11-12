class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        temp=node
        while temp.next:
            prev=temp
            temp.val=temp.next.val
            temp=temp.next
        prev.next=None
