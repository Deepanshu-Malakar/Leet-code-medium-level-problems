# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: object, n: int) -> object:
        temp=head
        count=0

        while(temp!=None):
            temp=temp.next
            count+=1

        pos=count-n+1
        temp=head

        if count == 1:
            return None
        
        if pos == 1:
            head=head.next
            return head
        
        for i in range(1,pos-1):
            temp=temp.next

        if(pos == count):
            temp.next=None
            return head
        
        temp.next=temp.next.next
        return head