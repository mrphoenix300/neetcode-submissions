from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key in self.time_map:
            left = 0
            right = len(self.time_map[key]) - 1
            target = -1
            while left <= right:
                mid = (left + right) // 2

                if self.time_map[key][mid][1] <= timestamp:
                    if self.time_map[key][mid][1] == timestamp:
                        return self.time_map[key][mid][0]
                    else:
                        target = mid
                        left = mid + 1
                else:
                    right = mid - 1
                
            if target != -1:
                return self.time_map[key][target][0]
        return ""
        
