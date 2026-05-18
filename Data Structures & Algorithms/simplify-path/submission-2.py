class Solution:
    def simplifyPath(self, path: str) -> str:
        
        split_path = path.split("/")
        stack = []

        for p in split_path:
            if p:
                if p != ".." and p != ".":
                    stack.append("/")
                    stack.append(p)
                else:
                    if stack and p == "..":
                        stack.pop()
                        if stack[-1] == "/":
                            stack.pop()
        
        if not stack:
            stack.append("/")

        simplified_path = "".join(stack)

        return simplified_path