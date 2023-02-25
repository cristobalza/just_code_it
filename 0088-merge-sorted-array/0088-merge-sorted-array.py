class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2: return None
        if not nums1:
            nums1 = nums2
            return None
        last = m + n - 1
        while n > 0 and m > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
            
        # while n > 0:
        #     nums1[last] = nums2[n - 1]
        #     n -= 1
        #     last -= 1
        for j in range(n - 1, -1, -1):
            nums1[last] = nums2[j]
            last -= 1