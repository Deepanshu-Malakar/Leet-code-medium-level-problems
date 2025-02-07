
"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12
"""

"""
Approach:
    if you have an array of just 1 element ex=[32]  then your answer = nums[0]
    if you have an array of just 2 elements ex=[32,10] then your answer = max(nums[0],nums[1])
    we can store these results in an array total_loot as [32,32]  total_loot[0] denotes the max loot upto 1st house = nums[0]
    total_loot[1] will denote the max loot upto house 2 = max(nums[0],nums[1])
    total_loot[2] will denote the max loot upto house 3 and soo on
    total_loot[i] = max(total_loot[i-2]+nums[i],total_loot[i-1])  
    if you want to loot the ith house then either consider the max loot upto i-2 and ith loot or consider max loot upto i-1

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        elif(len(nums)==1):
            return nums[0]
        #for more than 2
        array=[0 for i in range(0,len(nums))]
        array[0]=nums[0]
        array[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            array[i]=max(array[i-2]+nums[i],array[i-1])
        return array[len(nums)-1]