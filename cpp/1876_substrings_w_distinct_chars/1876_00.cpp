class Solution {
public:
  int countGoodSubstrings(string s) {
    int slen = s.size();
    int ans = 0;
    int left = 0;
    std::vector<char> winchar;
    for (int right = 0; right < slen; right++) {
      if (right < 2) {
	winchar.push_back(s[right]);
	continue;
      }

      winchar.push_back(s[right]);

      std::set<char> winset(winchar.begin(), winchar.end());
      if (winset.size() == 3) {
	ans += 1;
      }

      winchar.erase(winchar.begin());
      left++;

    }
    return ans;
  }
};
