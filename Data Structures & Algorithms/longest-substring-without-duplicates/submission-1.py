class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substring = set()
        longest_substring = 0

        for right in range(len(s)):
            left = right - 1
            if s[right] in substring:
                substring = set()
                while s[left] != s[right]:
                    substring.add(s[left])
                    left -= 1
            
            substring.add(s[right])


            longest_substring = max(len(substring), longest_substring)
        
        return longest_substring