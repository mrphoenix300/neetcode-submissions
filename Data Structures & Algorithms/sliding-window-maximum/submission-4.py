class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        maximum_window_elements = []
        window = deque()

        for i in range(len(nums)):
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)

            if window[0] < i - k + 1:
                window.popleft()
            
            if i >= k - 1:
                maximum_window_elements.append(nums[window[0]])
        
        return maximum_window_elements





        