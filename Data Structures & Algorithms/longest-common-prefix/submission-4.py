class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = strs[0]
        i = 0
        for s in strs:
            i = 0
            while i < len(temp) and i < len(s) and temp[i] == s[i]:
                i += 1
            temp = temp[:i]
        
        return temp