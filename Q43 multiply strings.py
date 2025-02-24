"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself
"""

class Solution:
    def int_to_string(self,n:int):
        s:str=""
        while(n>0):
            x=n%10
            n=n//10
            s=f"{x}"+s
        return s
    
    def string_to_int(self,s:str):
        n:int=0
        for i in s:
            n = n*10 + int(i)
        return n
    def multiply(self, num1: str, num2: str) -> str:
        #return str(int(num1)*int(num2))
        if(num1 == "0" or num2 == "0"):
            return "0"
        n1 = self.string_to_int(num1)
        n2 = self.string_to_int(num2)
        p = n1*n2
        return self.int_to_string(p)