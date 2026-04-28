class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()

        left = 0
        right = len(s) - 1
        mid = (left + right) // 2
        count = 0

        while left <= mid and right > mid:
            if s[left] == s[right]:
                count += 1
            else:
                return False
            left += 1
            right -= 1
        
        
        return True


