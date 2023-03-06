class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n, stack = len(intervals), []
        if n == 1: return intervals
        intervals.sort(key= lambda x : x[0])
        prev = intervals[0]
        stack.append(prev)
        for i in range(1, n):
            if prev[1] < intervals[i][0]:
                stack.append(intervals[i])
                prev = intervals[i]
            else:
                stack.pop()
                new_inter = [min(prev[0], intervals[i][0]), max(intervals[i][1], prev[1])]
                stack.append(new_inter)
                prev = new_inter
        return stack