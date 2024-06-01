--At first we extracted the 2 numbers from the linked lists in nm1 and nm2
---value of each node is multiplied with next power of 10 and added to get the required numbers
---example=[3,4,5]-->3+4*10+5*100=543

--then we add the 2 numbers
--now convert the number to string
--iterate the string and insert the digit to head of the linked list and 
--then connect the next digit to value of new node and make the new node the new head by connecting its .next=head
--head=newnode

--return the result