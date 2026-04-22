class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_of_anagrams = []
        tmp_strs = [string for string in strs]

        for i in range(len(tmp_strs)):
            tmp_strs[i] = "".join(sorted(tmp_strs[i]))

        anagrams = defaultdict(list)

        for index, string in enumerate(tmp_strs):
            if string in anagrams:
                anagrams[string].append(index)
            else:
                anagrams[string] = [index]

        i = 0
        for indices in anagrams.values():
            group_of_anagrams.append([])
            for index in indices:
                group_of_anagrams[i].append(strs[index])
            i += 1

        return group_of_anagrams

        