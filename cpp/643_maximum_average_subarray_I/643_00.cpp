class Solution {
public:
  double findMaxAverage(vector<int>& nums, int k) {
    int numlen = nums.size();
    if (numlen < 2) return (double) nums[0];
        
    int right = 0;
    int left = 0;
    int ans = 0;

    while (right < k) {
      ans += nums[right];
      right++;
    }
        
    int curr = ans;
    while (right < numlen) {
      curr += nums[right];
      curr -= nums[left];
      ans = std::max(ans, curr);
      right++;
      left++;
    }
    return ans / ((double) k);
  }
};
