from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        if key in self.time_map and timestamp in self.time_map[key]:
            return self.time_map[key][timestamp]
        elif key in self.time_map:
            searching_timestamp = timestamp - 1
            while searching_timestamp >= 0:
                if searching_timestamp in self.time_map[key]:
                    return self.time_map[key][searching_timestamp]
                searching_timestamp -= 1

        return ""
        
