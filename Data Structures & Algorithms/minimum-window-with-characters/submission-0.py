class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        left = 0
        target_map = Counter(t)
        need = len(target_map)
        min_len = float('inf')
        res = [-1, -1]
        have = 0
        window_map = {}
        for right in range(len(s)):
            char = s[right]
            window_map[char] = window_map.get(char, 0) + 1
            if char in target_map and window_map[char] == target_map[char]:
                have += 1
            while have == need:
                char = s[left]
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    res[0], res[1] = left, right
                if char in target_map and window_map[char] == target_map[char]:
                    have -= 1
                window_map[char] -= 1
                left += 1
            
        
        if min_len != float('inf'):
            return s[res[0]:res[1]+1]
        else:
            return ""
            
            




        