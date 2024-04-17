class Solution {
public:
  vector<int> decrypt(vector<int>& code, int k) {
    int codelen = code.size();
    std::vector<int> ans(codelen, 0);
    int i;
    for (int right = 0; right < codelen; right++) {
      i = 0;
      int idx;
      while (i < k) {
	idx = (right + (i+1)) % codelen;
	ans[right] += code[idx];
	i++;
      }
      while (i != std::abs(k) && i > k) {
	idx = (right - (i+1)) % codelen; 
	if (idx < 0) idx = codelen + idx;
	ans[right] += code[idx];
	i++;
      }

    }
    return ans;
  }
};
