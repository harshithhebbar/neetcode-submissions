# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=head
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        head=l
        a=a[::-1]
        i=0
        while head:
            head.val=a[i]
            i+=1
            head=head.next
        head=l
        return head