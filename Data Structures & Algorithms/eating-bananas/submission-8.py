class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # testout which numbers fit the best
        l, r = 1, max(piles)

        def time(speed):
            time = 0
            for pile in piles: 
                time += math.ceil(pile/speed)
            return time

        while l <= r: 
            mid = (l + r) // 2
            if time(mid) <= h: 
                if mid == 1 or time(mid - 1) > h: #time used bigger than have
                    return mid
                r = mid - 1 # get a bigger time

            else: l = mid + 1
            
        return r