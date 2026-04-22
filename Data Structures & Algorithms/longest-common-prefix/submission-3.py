class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        j = 0
        has_finished_string = False
        is_first_valid = True
        if len(strs[0]) == j:
            return longest_common_prefix
        while not has_finished_string:
            prefix = strs[0][j]
            is_same = True
            for k in range(1, len(strs)):
                if j < len(strs[k]):
                    if prefix != strs[k][j]:
                        if j == 0:
                            is_first_valid = False
                        is_same = False
                        break
                else:
                    has_finished_string = True
                    break
            
            if is_first_valid is False:
                break

            if has_finished_string:
                break

            if is_same:
                longest_common_prefix += prefix
            else:
                break
            
            j += 1
            if j >= len(strs[0]):
                has_finished_string = True
            
        return longest_common_prefix