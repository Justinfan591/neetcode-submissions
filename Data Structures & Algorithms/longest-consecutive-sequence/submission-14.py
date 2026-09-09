class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = {}   # only the endpoints of each run are guaranteed accurate
        best = 0
        for n in nums:
            if n in lengths:
                continue
            left = lengths.get(n - 1, 0)
            right = lengths.get(n + 1, 0)
            total = left + right + 1
            lengths[n] = total
            lengths[n - left] = total      # update the run's left endpoint
            lengths[n + right] = total     # update the run's right endpoint
            best = max(best, total)
        return best