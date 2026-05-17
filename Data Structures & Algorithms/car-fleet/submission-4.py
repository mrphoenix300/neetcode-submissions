class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = zip(position, speed)
        sorted_pairs = sorted(pairs, reverse=True)

        position_new, speed_new = zip(*sorted_pairs)

        position = list(position_new)
        speed = list(speed_new)
        print(position)
        print(speed)

        car_fleets = [(target - position[0])/speed[0]]

        for i in range(1, len(position)):
            time = (target - position[i])/speed[i]
            if time > car_fleets[-1]:
                car_fleets.append(time)

        return len(car_fleets)


        