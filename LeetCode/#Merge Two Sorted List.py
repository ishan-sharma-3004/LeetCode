#Merge Two Sorted List
'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        N=dummy=ListNode(0)
        while(list1!=None and list2 != None):
            if(list1.val<list2.val):
                N.next=list1
                list1=list1.next
            else:
                N.next=list2
                list2=list2.next
            N=N.next
        if list1!= None:
            N.next=list1
            list1=list1.next
        if list2!=None:
            N.next=list2
            list2=list2.next
            
        return dummy.next    