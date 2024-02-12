class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search horizontal and vertical
        m,  n = len(matrix), len(matrix[0])
        
        l, r = 0, m - 1
        find_row = -1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                find_row = mid
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][n - 1] < target:
                l = mid + 1
    
        if find_row == -1:
            return False
        
        arr = matrix[find_row]
        # print(arr)
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        
        return True if arr[r] == target else False
        