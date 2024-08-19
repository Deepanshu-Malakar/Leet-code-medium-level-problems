# 3. Longest Substring Without Repeating Characters
# Medium
# Topics
# Companies
# Hint
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=0
        max_length=0
        # greatest_substring=[]
        for i in range(0,len(s)):
            j=i
            while(j<len(s)-1 and s[j]!=s[j+1]):
                j=j+1
            
            if(max_length<i-j+1):
                max_length=i-j+1
                # greatest_substring.append(s[i:j+1])
        return max_length