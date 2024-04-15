
class Solution {
public:
  void reverseString(vector<char>& s) {
    long slen = s.size(); 
    if (slen < 2) {
      return;
    };
        
    char tmp;
    long front = 0;
    long back = slen-1;
    while (front < slen / 2) {
      std::swap(s[front], s[slen-1-front]);
      front++;
      back--;
    };
            
    return;        
        
  };
};
