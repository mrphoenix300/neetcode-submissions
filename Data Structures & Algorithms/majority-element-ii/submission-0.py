class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency_map = Counter(nums)

        majority_elements = []
        n = len(nums)
        for key, frequency in frequency_map.items():
            if frequency > n // 3:
                majority_elements.append(key)
        
        return majority_elements