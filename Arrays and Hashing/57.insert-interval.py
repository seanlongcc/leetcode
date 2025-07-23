#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        n = len(intervals)

        # add intervals starting before newinterval to merged
        # check if the 2nd element in the first interval is less than the first element of the new intervals
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # merge all interlapping intervals
        # check if the 1st element in the interval is <= the 2nd element of new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            # compare each 1st value to get the minimum interval
            newInterval[0] = min(intervals[i][0], newInterval[0])
            # compare each 2nd value to get the maximum interval
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        # append the new interval
        merged.append(newInterval)

        # add on the rest of the intervals
        for j in range(i, n):
            merged.append(intervals[j])

        return merged
# @lc code=end
