#Add Two Numbers
#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        listr=None
        temp=None
        carry=0
        while(l1!=None or l2!=None):
            sum=carry
            if(l1!=None):
                sum+=l1.val
                l1=l1.next
            if(l2!=None):
                sum+=l2.val
                l2=l2.next
            new=ListNode(sum%10)
            carry=sum//10
            if temp==None:
                temp=listr=new
            else:
                temp.next=new
                temp=temp.next

        if carry>0:
            temp.next=ListNode(carry)
        return listr