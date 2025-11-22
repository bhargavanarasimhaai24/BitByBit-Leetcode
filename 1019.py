class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        n=len(arr)
        res=[0]*n
        stack=[]
        for i in range(n):
            while stack and arr[i]>arr[stack[-1]]:
                idx=stack.pop()
                res[idx]=arr[i]
            stack.append(i)
        return res
