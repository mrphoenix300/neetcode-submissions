class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        maximum_window_elements = []
        window = deque()
        max_element = nums[0]

        for i in range(len(nums)):
            window.append(nums[i])
            if len(window) == k:
                max_element = max(window)
                maximum_window_elements.append(max_element)
                window.popleft()
        
        return maximum_window_elements





        