class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n, stack = len(intervals), []
        if n == 1: return intervals
        intervals.sort(key= lambda x : x[0])
        stack.append(intervals[0])
        for i in range(1, n):
            if stack[-1][1] < intervals[i][0]:
                stack.append(intervals[i])
            else:
                prev = stack.pop()
                stack.append([min(prev[0], intervals[i][0]), max(prev[1], intervals[i][1])])
        return stack