class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        length_of_arr = mountainArr.length()
        l, r = 0, length_of_arr - 1
        min_index = length_of_arr
        calls = 0

        while l <= r and calls < 100:
            mid = (l + r) // 2

            value = mountainArr.get(mid)
            calls += 1

            if value == target:
                min_index = min(mid, min_index)
                if min_index == 0:
                    break
                l = 0
                r = mid - 1
                if r == -1:
                    break
            elif value > target:
                if mid + 1 < length_of_arr:
                    next_value = mountainArr.get(mid + 1)
                else:
                    l = 0
                    r = mid - 1
                    continue
                calls += 1
                if next_value > value:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if mid + 1 < length_of_arr:
                    next_value = mountainArr.get(mid + 1)
                else:
                    l = 0
                    r = mid - 1
                    continue
                calls += 1
                if next_value > value:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return min_index if min_index != length_of_arr else -1


        