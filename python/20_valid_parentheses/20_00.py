par_char = ["(", ")", "[", "]", "{", "}"]
par_pair = {"(": ")", "[": "]", "{": "}"}
class Solution:
    def isValid(self, s: str) -> bool:

        open_list = list(par_pair.keys())
        close_list = list(par_pair.values())
        if s[0] in close_list:
            return False

        mismatched_pairs = [s[0]]
        for ch in s[1:]: 

            if ch in open_list:
                mismatched_pairs.append(ch)
            else:
                if len(mismatched_pairs) == 0:
                    return False
                    
                if ch == par_pair[mismatched_pairs[-1]]:
                    mismatched_pairs.pop(-1)
                else:
                    return False

        if len(mismatched_pairs) == 0:
            return True
        else:
            return False
