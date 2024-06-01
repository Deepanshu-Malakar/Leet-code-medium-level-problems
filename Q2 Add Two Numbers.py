"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: object[ListNode], l2: object[ListNode]) -> object[ListNode]:
        i=l1
        j=l2
        nm1=0
        nm2=0
        c=0
        while i:
            nm1+=i.val*10**c
            i=i.next
            c=c+1
        c=0
        while j:
            nm2+=j.val*10**c
            j=j.next
            c=c+1
        s=str(nm1+nm2)
        head=ListNode(s[0])
        for i in range(1,len(s)):
            x=ListNode(s[i],head)
            head=x
        return head