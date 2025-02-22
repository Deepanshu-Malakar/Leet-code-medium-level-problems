#include<bits/stdc++.h>
using namespace std;

class Solution {
    public:
        void reverse(vector<int> &v,int low,int high){
            int n=v.size();
            int i=low;
            int j=high;
            while(i<j){
                swap(v[i],v[j]);
                i++;
                j--;
            }
        }
        void nextPermutation(vector<int>& nums) {
            int size = nums.size();
            if(size == 1){
                return; 
            }
            else if(size == 2){
                swap(nums[0],nums[1]);
                return;
            }
            int i = size-2;
            while(i>=0 && nums[i]>=nums[i+1]){
                i--;
            }
            if(i==-1){
                reverse(nums,0,size-1);
                return;
            }
            int j = i+1;
            while(j<=size-1 && nums[j]>nums[i]){
                j++;
            }
            j--;
            swap(nums[i],nums[j]);
            reverse(nums,i+1,size-1);
            return;
        }
    };