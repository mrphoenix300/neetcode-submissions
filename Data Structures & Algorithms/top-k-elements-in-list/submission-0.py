class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        top_k = []
        for i in range(1, k + 1):
            max_element = max(frequency_map, key=frequency_map.get)
            top_k.append(max_element)
            frequency_map.pop(max_element)
        
        return top_k

        