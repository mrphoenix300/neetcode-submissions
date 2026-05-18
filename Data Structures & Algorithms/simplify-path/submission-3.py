class Solution:
    def simplifyPath(self, path: str) -> str:
        
        split_path = path.split("/")
        stack = []

        for p in split_path:
            if p:
                if p != ".." and p != ".":
                    stack.append(p)
                else:
                    if stack and p == "..":
                        stack.pop()

        simplified_path = "/" + "/".join(stack)

        return simplified_path