class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = []
        brackets = {"(": ")", "[": "]", "{": "}"}

        for i in range(len(s)):
            if s[i] in brackets:
                stack.append(s[i])
            else:
                if stack:
                    if brackets[stack[-1]] == s[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return True if not stack else False
        