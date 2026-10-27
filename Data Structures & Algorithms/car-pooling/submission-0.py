class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        stops = [0] * 1001

        for passengers, start, end in trips:
            stops[start] += passengers
            stops[end] -= passengers

        current = 0

        for change in stops:
            current += change
            if current > capacity:
                return False

        return True