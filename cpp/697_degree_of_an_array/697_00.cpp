class Solution {
public:
  int findShortestSubArray(vector<int>& nums) {
    int const numlen = nums.size();
    int ans = numlen;

    // find degree
    //
    std::unordered_map<int, int> counter;
    for (int const num: nums) {
      counter[num]++;
    }
        
    int order = 0;
    std::map<int, int> tmp_cntr;
    for (auto const & [key, val]: counter) {
      order = std::max(order, val);
    }

    int left = 0;
    for (int right = 0; right < numlen; right++) {
      tmp_cntr[nums[right]]++;
            
      while (tmp_cntr[nums[right]] == order) {
	ans = std::min(ans, right - left + 1);
	if (ans == order) return ans;
	tmp_cntr[nums[left]] -= 1;
	left++;
      }

            
    }

    return ans;
  }
};
