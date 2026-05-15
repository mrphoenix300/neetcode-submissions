class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            is_inside = False
            while stack:
                if temperature > stack[-1][1]:
                    temp = stack.pop()
                    result[temp[0]] = i - temp[0]
                else:
                    is_inside = True
                    stack.append([i, temperature])
                    break
            if not is_inside:
                stack.append([i, temperature])

        return result
