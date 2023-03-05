class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda interval:interval[0])
        n, res, prev_time = len(intervals), 0, intervals[0][1]
        for i in range(1, n):
            if prev_time <= intervals[i][0]:
                prev_time = intervals[i][1]
            else:
                res += 1
                if prev_time < intervals[i][1]:
                    continue
                else:
                    prev_time = intervals[i][1]
        return res
        