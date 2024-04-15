#include <cmath>

class Solution {
public:
  vector<int> sortedSquares(vector<int>& nums) {
    int numlen = nums.size();
    vector<int> outarr(numlen);
    if (numlen < 2) {
      for (int i: nums) {
	outarr[0] = pow(i, 2);
      }
      return outarr;  
    }
        
    // find the zero index
    //
    int zidx = 0;
    while (zidx < numlen && nums[zidx] < 0) {
      zidx++;
    }
        
    int left, right;
    left = zidx - 1;
    right = zidx;
    int i = 0;
    while (i < numlen) {
            
      if (right == numlen) {
	outarr[i] = pow(nums[left], 2);
	left--;
	i++;
	continue;
      }
      if (left < 0) {
	outarr[i] = pow(nums[right], 2);
	right++;
	i++;
	continue;
      }
            
      if (nums[right] > abs(nums[left])) {
	outarr[i] = pow(nums[left], 2);
	left--;
      } else if (nums[right] <= abs(nums[left])) {
	outarr[i] = pow(nums[right], 2);
	right++;
      } 
      i++;
    }
        
    return outarr;

  }
};
