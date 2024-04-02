class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        prev = ""
        for i in range(len(s)):
            if (s[i].lower() == prev and prev.islower() and s[i].isupper()) or (s[i].upper() == prev and prev.isupper() and s[i].islower()):
                stack.pop()
            else:
                stack.append(s[i])
            
            prev = stack[-1] if len(stack) else ""
            
        return "".join(stack)
