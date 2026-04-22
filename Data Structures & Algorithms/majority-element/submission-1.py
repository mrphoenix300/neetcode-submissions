class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency_dict = Counter(nums)
        max_key = max(frequency_dict, key=frequency_dict.get)

        return max_key