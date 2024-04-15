class Solution {
public:
  bool isSubsequence(string s, string t) {
        
    if (s.size() == 0 && t.size() == 0) {
      return true;
    };

    short slow = 0;
    for (short fast = 0; fast < t.size(); fast++) {

      if (t[fast] == s[slow]) {
	slow++;
      };

      if (slow == s.size()) {
	return true;
      };
    };

    return false;
  };
};
