class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                left_part = s[left+1:right+1]
                right_part = s[left:right]
                return left_part == left_part[::-1] or right_part == right_part[::-1]
            left += 1
            right -= 1
        

        return True
        