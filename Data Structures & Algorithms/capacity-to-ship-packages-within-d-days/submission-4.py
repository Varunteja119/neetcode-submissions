class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysNeeded(capacity):
            ships, c = 1, capacity
            for w in weights:
                if c - w < 0:
                    ships += 1
                    c = capacity
                c -= w
            return ships
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            if daysNeeded(mid) <= days:
                r = mid
            else:
                l = mid + 1
        return l