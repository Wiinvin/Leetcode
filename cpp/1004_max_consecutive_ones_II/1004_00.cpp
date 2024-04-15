class Solution {
public:
  int longestOnes(vector<int>& nums, int k) {
        
    int numlen = nums.size();
    if (numlen < 0) return 0;
        
    int left = 0;
    int curr = 0;
    int ans = 0;        
    for (int right = 0; right < numlen; right++) {
      if (nums[right] == 0) {
	curr++;
      }
      while (curr > k) {
	if (nums[left] == 0) {
	  curr--;
	}
	left++;
      }
            
      ans = std::max(ans, right - left + 1);
            
    }
    return ans;
  }
};
