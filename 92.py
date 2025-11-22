# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self):
        self.new = None

    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        temp = head
        self.new = None
        before = None  
        for i in range(left - 1):
            before = temp
            temp = temp.next
        start = temp        
        for i in range(right - left + 1):
            nxt = temp.next
            temp.next = self.new
            self.new = temp
            temp = nxt
        start.next = temp  
        if before:
            before.next = self.new  
        else:
            head = self.new      

        return head
