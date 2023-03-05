class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda interval:interval[0])
        n, res, prev = len(intervals), 0, intervals[0][1]
        for i in range(1, n):
            if prev <= intervals[i][0]:
                prev = intervals[i][1]
            else:
                res += 1
                if prev < intervals[i][1]:
                    continue
                else:
                    prev = intervals[i][1]
        return res
        