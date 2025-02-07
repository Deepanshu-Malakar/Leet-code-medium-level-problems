"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=[]
        for i in range(0,len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j:int = i+1
            k:int = len(nums)-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if(sum>0):
                    k-=1
                elif(sum<0):
                    j+=1
                else:
                    x=[nums[i],nums[j],nums[k]]
                    l.append(x)
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j=j+1
                    while(j<k and nums[k]==nums[k+1]):
                        k=k-1
        return l