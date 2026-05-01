class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = defaultdict(list)
        for i in range(len(nums)):
            index_map[nums[i]].append(i)

        for num in nums:
            if len(index_map[num]) == 1:
                index_map.pop(num)

        for indices in index_map.values():
            i = 0
            for j in range(i + 1, len(indices)):
                if abs(indices[i] - indices[j]) <= k:
                    return True
                i += 1
        return False