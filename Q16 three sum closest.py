"""
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=20000
        closest_sum=20000
        for i in range(0,len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if(sum > target):
                    if(sum - target < closest):
                        closest = sum - target
                        closest_sum=sum
                    k=k-1
                elif(sum < target):
                    if( target - sum <closest):
                        closest = target - sum
                        closest_sum=sum
                    j=j+1
                else:
                    return target
        return closest_sum
      