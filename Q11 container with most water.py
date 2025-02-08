"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        pillar1=0
        pillar2=len(height)-1
        maxarea=0
        while(pillar1<pillar2):
            area = (pillar2 - pillar1)*min(height[pillar1],height[pillar2])
            if(area>maxarea):
                maxarea = area
            if(height[pillar1]>height[pillar2]):
                pillar2=pillar2-1
            else:
                pillar1=pillar1+1
        return maxarea