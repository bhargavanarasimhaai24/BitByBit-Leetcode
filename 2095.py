class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        fast=head
        slow=head
        prev=None
        if not head.next:
            return None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        slow.next=None
        return head
