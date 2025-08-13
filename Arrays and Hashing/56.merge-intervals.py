#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        intervals.sort(key=lambda x: x[0])

        for start, end in intervals:
            # If merged is empty OR current interval starts after the last merged interval ends,
            # there is no overlap → add it as a new interval.
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                # Overlap exists → merge by extending the end time of the last merged interval
                # to the later of the two end times.
                merged[-1][1] = max(end, merged[-1][1])

        # @lc code=end
