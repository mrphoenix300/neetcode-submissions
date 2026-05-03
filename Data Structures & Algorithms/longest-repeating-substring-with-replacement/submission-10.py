class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        max_length = 0
        max_freq = 0
        left = 0
        for right in range(len(s)):
            if s[right] in freq_map:
                freq_map[s[right]] += 1
            else:
                freq_map[s[right]] = 1
            
            max_freq = max(freq_map[s[right]], max_freq)

            if (right - left + 1) - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1
            
            max_length = max(right - left + 1, max_length)
        
        return max_length

        




