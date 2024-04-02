class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        
        while i < len(path):
            if path[i] == '/':
                i += 1
                continue
                
            dir = ""
            while i < len(path) and path[i] is not "/":
                dir += path[i]
                i += 1

            if dir == "..":
                if len(stack) > 0:
                    stack.pop()
            elif dir == ".":
                pass
            else: 
                stack.append(dir)



        return "/" + "/".join(stack) if len(stack) != 0 else "/"
