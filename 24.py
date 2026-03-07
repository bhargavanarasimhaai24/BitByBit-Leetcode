# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        else:
            p1=head
            p2=head.next
            p1.next=self.swapPairs(p2.next)
            p2.next=p1
            return p2
