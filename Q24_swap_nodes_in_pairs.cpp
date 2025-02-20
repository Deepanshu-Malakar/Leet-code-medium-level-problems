#include <bits/stdc++.h>
using namespace std;

/*
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]
*/

// Definition for singly-linked list.
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *swapPairs(struct ListNode *head)
{
    struct ListNode *temp = head;
    if (temp == NULL)
    {
        return NULL;
    }
    else if (temp->next == NULL)
    {
        return temp;
    }
    head = temp->next;
    struct ListNode *prev = NULL;
    while (temp != NULL && temp->next != NULL)
    {
        struct ListNode *next = temp->next;
        temp->next = next->next;
        next->next = temp;
        if (prev != NULL)
        {
            prev->next = next;
        }
        prev = temp;
        temp = temp->next;
    }
    return head;
}